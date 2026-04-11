"""
Agentic loop with streaming SSE output.

Events emitted (JSON, one per SSE data line):
  {"type": "text",        "content": "..."}   – streamed text delta
  {"type": "tool_start",  "name": "..."}       – Claude is calling a tool
  {"type": "tool_done",   "name": "...", "preview": "..."}  – tool result summary
  {"type": "cost",        "input_tokens": N, "output_tokens": N, "cost_usd": N}  – usage summary
  {"type": "done"}                             – conversation turn finished
  {"type": "error",       "content": "..."}   – something went wrong
"""
import json
import re
from typing import AsyncGenerator

import anthropic
from dotenv import load_dotenv

from app.skills_config import get_skill_ids, get_skill_names
from app.tools import TOOL_DEFINITIONS, execute_tool

load_dotenv()

SYSTEM_PROMPT = """Du bist ein juristischer Rechercheassistent, spezialisiert auf Schweizer Strafrecht.

Du hast Zugriff auf folgende Recherchequellen und -werkzeuge:

**Lokale Datenbank**
- `list_regesten` – listet alle verfügbaren internen Präjudizen (Titel und Regeste) auf, nützlich für einen Überblick
- `get_praejudiz` – ruft die kompletten Details (inkl. Urteilsauszug) eines Präjudizes anhand des Titels ab
- `search_local_cases` – interne Präjudizen des Kriminalgerichts Luzern nach Stichworten durchsuchen

**OpenCaseLaw – Entscheide (956'000+)**
- `search_decisions` – Volltextsuche mit Booleschen Operatoren, Gericht- und Datumsfiltern
- `find_leading_cases` – meistzitierte Leitentscheide zu einem Thema oder Gesetzesartikel
- `get_decision` – Volltext eines einzelnen Entscheids
- `get_case_brief` – strukturiertes Case Brief (Sachverhalt, Erwägungen, Dispositiv)
- `find_citations` – Zitationsanalyse (wer zitiert wen)
- `find_appeal_chain` – Instanzenzug eines Entscheids

**OpenCaseLaw – Gesetze**
- `get_law` – Gesetzesartikeltext (StGB, StPO, BV, OR usw.)
- `search_laws` – Artikelsuche über alle Bundesgesetze

**OpenCaseLaw – Doktrin & Kommentare**
- `get_doctrine` – Leitentscheide + Dogmatik-Zeitleiste zu einem Artikel oder Rechtsbegriff
- `get_commentary` – Wissenschaftlicher Kommentar (OnlineKommentar.ch) zu einem Gesetzesartikel
- `search_commentaries` – Volltextsuche in allen Kommentaren

**OpenCaseLaw – Analyse**
- `analyze_legal_trend` – Entwicklung der Rechtsprechung über die Jahre

Vorgehen:
1. Suche zuerst mit `search_local_cases` nach internen Präjudizen
2. Nutze `find_leading_cases` oder `get_doctrine` für die massgebliche Rechtsprechung
3. Hole mit `get_decision` oder `get_case_brief` die Details zu wichtigen Entscheiden
4. Ziehe bei Bedarf `get_law` für den Gesetzestext und `get_commentary` für die Doktrin bei
5. Verwende `find_citations` oder `find_appeal_chain` für vertiefende Analyse
6. Fasse die Ergebnisse präzise zusammen und weise auf die relevanten Rechtsfragen hin
7. Verlinke auf Entscheide. Nutze immer und ausschliesslich die `url`, die von den OpenCaseLaw-Werkzeugen im Ergebnis zurückgegeben wird. Erstelle keine eigenen Links (z.B. bger.li oder direkte opencaselaw.ch-Pfade), falls keine URL im Tool-Resultat vorhanden ist. Die Verlinkungen sollen so gestaltet sein, dass sie sich in einem neuen Fenster öffnen.
8. Antworte immer auf Deutsch"""


async def stream_chat(
    history: list[dict],
    user_message: str,
) -> AsyncGenerator[str, None]:
    """
    Runs the agentic loop and yields SSE-formatted strings.
    history: list of prior {role, content} dicts
    user_message: the new user input
    """
    client = anthropic.AsyncAnthropic()

    messages = history + [{"role": "user", "content": user_message}]

    # Pricing for claude-sonnet-4-5 (USD per million tokens)
    INPUT_COST_PER_M = 3.0
    OUTPUT_COST_PER_M = 15.0

    total_input_tokens = 0
    total_output_tokens = 0

    try:
        # Yield an initial space or newline to "prime" the stream and flush buffers.
        # This helps some proxies (like Firebase) to start streaming immediately.
        # 4096 bytes is a common buffer size for many enterprise proxies.
        yield ":" + " " * 4096 + "\n\n"
        
        skill_ids = get_skill_ids()
        skill_names = get_skill_names()
        code_execution_tool = {"type": "code_execution_20250825", "name": "code_execution"}

        turn_count = 0
        while True:
            turn_count += 1
            if turn_count > 1:
                yield _sse({"type": "status", "text": "Verarbeite Zwischenergebnisse…"})
            if skill_ids:
                stream_cm = client.beta.messages.stream(
                    model="claude-sonnet-4-5",
                    max_tokens=8192,
                    system=SYSTEM_PROMPT,
                    thinking={"type": "enabled", "budget_tokens": 4096},
                    tools=TOOL_DEFINITIONS + [code_execution_tool],
                    messages=messages,
                    betas=["skills-2025-10-02", "code-execution-2025-08-25"],
                    container={
                        "skills": [
                            {"type": "custom", "skill_id": sid, "version": "latest"}
                            for sid in skill_ids
                        ]
                    },
                )
            else:
                stream_cm = client.messages.stream(
                    model="claude-sonnet-4-5",
                    max_tokens=8192,
                    system=SYSTEM_PROMPT,
                    tools=TOOL_DEFINITIONS,
                    messages=messages,
                    thinking={"type": "enabled", "budget_tokens": 4096},
                )
            async with stream_cm as stream:
                first_delta_in_turn = True
                # server_tool_use id → block index (für code_execution)
                server_tool_id_to_index: dict[str, int] = {}
                # result block index → skill block index
                result_to_skill: dict[int, int] = {}
                # code_exec block index → accumulated code JSON
                code_exec_buffer: dict[int, str] = {}
                # skill block indices still awaiting done
                active_skill_indices: set[int] = set()

                async for event in stream:
                    if event.type == "content_block_start":
                        block_type = getattr(event.content_block, "type", "")
                        block_name = getattr(event.content_block, "name", "")
                        block_id   = getattr(event.content_block, "id", "")
                        tool_use_id = getattr(event.content_block, "tool_use_id", "")

                        if block_type in ("server_tool_use", "tool_use") and block_name == "code_execution":
                            # Skill startet: Code wird an den Container geschickt
                            code_exec_buffer[event.index] = ""
                            if block_id:
                                server_tool_id_to_index[block_id] = event.index
                            active_skill_indices.add(event.index)
                            yield _sse({
                                "type": "skill_event",
                                "action": "start",
                                "index": event.index,
                                "skills": skill_names,
                                "files": [],
                            })
                        elif block_type in ("server_tool_use", "tool_use"):
                            # Normales Tool startet
                            yield _sse({
                                "type": "tool_start",
                                "name": block_name,
                                "index": event.index
                            })
                        elif block_type == "thinking":
                            yield _sse({
                                "type": "thinking_start",
                                "index": event.index
                            })

                        elif block_type == "bash_code_execution_tool_result":
                            # Ergebnis eines code_execution-Calls → skill_idx ermitteln
                            skill_idx = server_tool_id_to_index.get(tool_use_id, None)
                            if skill_idx is not None:
                                result_to_skill[event.index] = skill_idx

                        elif block_type not in (
                            "text", "tool_use", "server_tool_use",
                            "thinking", "redacted_thinking", "bash_code_execution_tool_result",
                        ):
                            # Unbekannter nicht-text Block als Fallback
                            active_skill_indices.add(event.index)
                            yield _sse({
                                "type": "skill_event",
                                "action": "start",
                                "index": event.index,
                                "skills": skill_names,
                                "files": [],
                            })

                    elif event.type == "content_block_delta":
                        if event.delta.type == "text_delta":
                            yield _sse({"type": "text", "content": event.delta.text})
                        elif event.index in code_exec_buffer:
                            code_exec_buffer[event.index] += getattr(event.delta, "partial_json", "")
                        elif event.delta.type == "input_json_delta":
                            yield _sse({
                                "type": "tool_input_delta",
                                "index": event.index,
                                "delta": getattr(event.delta, "partial_json", "")
                            })
                        elif event.delta.type == "thinking_delta":
                            yield _sse({
                                "type": "thinking_delta",
                                "index": event.index,
                                "delta": getattr(event.delta, "thinking", "")
                            })

                    elif event.type == "content_block_stop":
                        if event.index in result_to_skill:
                            # Ergebnis-Block fertig → Skill abgeschlossen
                            skill_idx = result_to_skill.pop(event.index)
                            code = code_exec_buffer.pop(skill_idx, "")
                            matches = re.findall(r"/skills/([^/'\"\\\s]+)/([^'\"\)\\\s]+)", code)
                            files = [f"{s}/{f}" for s, f in matches]
                            active_skill_indices.discard(skill_idx)
                            yield _sse({
                                "type": "skill_event",
                                "action": "done",
                                "index": skill_idx,
                                "files": files,
                            })
                        elif event.index in active_skill_indices:
                            # server_tool_use block gestoppt, aber Ergebnis-Block folgt noch
                            # Pill bleibt mit Spinner, bis result_to_skill für diesen Index done auslöst.
                            # Falls kein Ergebnis-Block erwartet wird (kein Eintrag in result_to_skill),
                            # sofort als done markieren.
                            expected = event.index in server_tool_id_to_index.values()
                            if not expected:
                                active_skill_indices.discard(event.index)
                                code_exec_buffer.pop(event.index, None)
                                yield _sse({"type": "skill_event", "action": "done", "index": event.index})
                        else:
                            code_exec_buffer.pop(event.index, None)

                final = await stream.get_final_message()

            total_input_tokens += final.usage.input_tokens
            total_output_tokens += final.usage.output_tokens

            # Append assistant turn to history
            messages.append({"role": "assistant", "content": final.content})

            if final.stop_reason != "tool_use":
                break

            # Execute all requested tools
            tool_results = []
            for idx, block in enumerate(final.content):
                if block.type != "tool_use":
                    continue

                result_text = await execute_tool(block.name, block.input)

                yield _sse({
                    "type": "tool_done",
                    "index": idx,
                    "name": block.name,
                    "input": block.input,
                    "result": result_text
                })

                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result_text,
                })

            messages.append({"role": "user", "content": tool_results})

        cost_usd = (total_input_tokens * INPUT_COST_PER_M + total_output_tokens * OUTPUT_COST_PER_M) / 1_000_000
        yield _sse({
            "type": "cost",
            "input_tokens": total_input_tokens,
            "output_tokens": total_output_tokens,
            "cost_usd": round(cost_usd, 6),
        })
        yield _sse({
            "type": "done",
            "tokens_input": total_input_tokens,
            "tokens_output": total_output_tokens,
            "cost_usd": cost_usd
        })

    except Exception as e:
        yield _sse({"type": "error", "content": str(e)})


def _sse(payload: dict) -> str:
    return f"data: {json.dumps(payload, ensure_ascii=False)}\n\n"
