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

    # Pricing for claude-haiku-4-5 (USD per million tokens)
    INPUT_COST_PER_M = 1.0
    OUTPUT_COST_PER_M = 5.0

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
            if skill_ids:
                stream_cm = client.beta.messages.stream(
                    model="claude-haiku-4-5",
                    max_tokens=4096,
                    system=SYSTEM_PROMPT,
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
                    model="claude-haiku-4-5",
                    max_tokens=4096,
                    system=SYSTEM_PROMPT,
                    tools=TOOL_DEFINITIONS,
                    messages=messages,
                )
            async with stream_cm as stream:
                first_delta_in_turn = True
                active_skill_indices: set[int] = set()
                # Accumulate code_execution input to extract skill file references
                code_exec_buffer: dict[int, str] = {}

                async for event in stream:
                    if event.type == "content_block_start":
                        block_type = getattr(event.content_block, "type", "")
                        name = getattr(event.content_block, "name", "")

                        if block_type == "tool_use" and name == "code_execution":
                            # Akkumuliere Input, um später Skill-Dateien zu erkennen
                            code_exec_buffer[event.index] = ""

                        elif block_type not in ("text", "tool_use", "thinking", "redacted_thinking"):
                            # z.B. bash_code_execution_tool_result → Skill läuft gerade
                            active_skill_indices.add(event.index)
                            # Extrahiere /skills/<name>/<datei> aus akkumuliertem Code
                            code = next(iter(code_exec_buffer.values()), "")
                            matches = re.findall(r"/skills/([^/'\"\\\s]+)/([^'\"\)\\\s]+)", code)
                            files = [f"{s}/{f}" for s, f in matches] if matches else []
                            yield _sse({
                                "type": "skill_event",
                                "action": "start",
                                "index": event.index,
                                "skills": skill_names,
                                "files": files,
                            })

                    elif event.type == "content_block_delta":
                        if event.delta.type == "text_delta":
                            if turn_count > 1 and first_delta_in_turn:
                                yield _sse({"type": "text", "content": "\n\n"})
                            first_delta_in_turn = False
                            yield _sse({"type": "text", "content": event.delta.text})
                        elif event.index in code_exec_buffer:
                            code_exec_buffer[event.index] += getattr(event.delta, "partial_json", "")

                    elif event.type == "content_block_stop":
                        code_exec_buffer.pop(event.index, None)
                        if event.index in active_skill_indices:
                            active_skill_indices.discard(event.index)
                            yield _sse({"type": "skill_event", "action": "done", "index": event.index})

                final = await stream.get_final_message()

            total_input_tokens += final.usage.input_tokens
            total_output_tokens += final.usage.output_tokens

            # Append assistant turn to history
            messages.append({"role": "assistant", "content": final.content})

            if final.stop_reason != "tool_use":
                break

            # Execute all requested tools
            tool_results = []
            for block in final.content:
                if block.type != "tool_use":
                    continue

                yield _sse({"type": "tool_start", "name": block.name, "input": block.input})

                result_text = await execute_tool(block.name, block.input)

                yield _sse({"type": "tool_done", "name": block.name, "result": result_text})

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
