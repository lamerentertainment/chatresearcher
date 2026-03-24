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
import os
from typing import AsyncGenerator

import anthropic
from dotenv import load_dotenv

from app.tools import TOOL_DEFINITIONS, execute_tool

load_dotenv()

SYSTEM_PROMPT = """Du bist ein juristischer Rechercheassistent, spezialisiert auf Schweizer Strafrecht.

Du hast Zugriff auf folgende Recherchequellen und -werkzeuge:

**Lokale Datenbank**
- `search_local_cases` – interne Präjudizen des Kriminalgerichts Luzern

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
7. Verlinke nach Möglichkeit auf die gefundenen Urteile unter Verwendung von Markdown-Links (z.B. `[BGer 6B_1234/2025](https://opencaselaw.ch/bger_6B_1234_2025)`). Nutze die `decision_id` aus den Tool-Ergebnissen für die URL-Struktur `https://opencaselaw.ch/<decision_id>`.
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
        yield ":" + " " * 2048 + "\n\n"
        
        turn_count = 0
        while True:
            turn_count += 1
            async with client.messages.stream(
                model="claude-haiku-4-5",
                max_tokens=4096,
                system=SYSTEM_PROMPT,
                tools=TOOL_DEFINITIONS,
                messages=messages,
            ) as stream:
                # Stream text deltas to the client
                first_delta_in_turn = True
                async for text in stream.text_stream:
                    if turn_count > 1 and first_delta_in_turn:
                        yield _sse({"type": "text", "content": "\n\n"})
                        first_delta_in_turn = False
                    yield _sse({"type": "text", "content": text})

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
