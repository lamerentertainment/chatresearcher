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

Du hast Zugriff auf zwei Recherchequellen:
1. **Lokale Präjudizen-Datenbank** – interne Entscheide des Kriminalgerichts Luzern
2. **OpenCaseLaw** – öffentliche Schweizer Gerichtsentscheide (BGer, Kantonsgerichte, 956k+ Entscheide)

Vorgehen:
- Suche zuerst in der lokalen Datenbank nach internen Präjudizen
- Ergänze anschliessend mit relevanten öffentlichen Entscheiden via OpenCaseLaw
- Fasse die gefundenen Entscheide präzise zusammen und weise auf die relevanten Rechtsfragen hin
- Antworte immer auf Deutsch"""


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
        while True:
            async with client.messages.stream(
                model="claude-haiku-4-5",
                max_tokens=4096,
                system=SYSTEM_PROMPT,
                tools=TOOL_DEFINITIONS,
                messages=messages,
            ) as stream:
                # Stream text deltas to the client
                async for text in stream.text_stream:
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
        yield _sse({"type": "done"})

    except Exception as e:
        yield _sse({"type": "error", "content": str(e)})


def _sse(payload: dict) -> str:
    return f"data: {json.dumps(payload, ensure_ascii=False)}\n\n"
