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
import re
from pathlib import Path
from typing import AsyncGenerator, Optional

import anthropic
import httpx
from dotenv import load_dotenv

from app.skills_config import get_skill_ids, get_skill_names
from app.tools import TOOL_DEFINITIONS, execute_tool

load_dotenv()
HERMES_API_KEY = os.getenv("HERMES_API_KEY")
HERMES_URL = os.getenv("HERMES_URL", "http://localhost:8642/v1")
HERMES_REMOTE_URL = os.getenv("HERMES_REMOTE_URL")
HERMES_REMOTE_API_KEY = os.getenv("HERMES_REMOTE_API_KEY")


def _load_local_skills() -> str:
    """Reads all SKILL.md files from the skills/ directory and returns an aggregated prompt string."""
    skills_dir = Path(__file__).parent.parent / "skills"
    all_content = []
    if skills_dir.exists():
        for skill_path in skills_dir.rglob("SKILL.md"):
            try:
                content = skill_path.read_text()
                # Include the parent folder name as context for the skill
                all_content.append(f"### Skill: {skill_path.parent.name}\n{content}")
            except Exception:
                continue
    if not all_content:
        return ""
    return "\n\n--- LOCAL SKILLS ---\n\n" + "\n\n".join(all_content)

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



class HermesProvider:
    """Handles interaction with the local Hermes Agent SDK Gateway."""

    def __init__(self, url: str = "http://localhost:8642/v1", api_key: Optional[str] = None):
        self.url = url
        headers = {}
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"
        self.client = httpx.AsyncClient(timeout=600.0, headers=headers)

    def _convert_tools(self, anthropic_tools: list) -> list:
        """Converts Anthropic tool definitions to OpenAI/Hermes compatible format."""
        openai_tools = []
        for tool in anthropic_tools:
            if tool.get("type") == "code_execution_20250825":
                continue # Skip specialized Anthropic tools
            
            openai_tools.append({
                "type": "function",
                "function": {
                    "name": tool["name"],
                    "description": tool["description"],
                    "parameters": tool["input_schema"]
                }
            })
        return openai_tools

    async def chat_stream(self, messages: list, system_prompt: str):
        """Streams from Hermes and handles thinking tags."""
        # Inject local skills into system prompt for Hermes
        local_skills = _load_local_skills()
        full_system = system_prompt + local_skills
        
        payload = {
            "model": "hermes",
            "messages": [{"role": "system", "content": full_system}] + messages,
            "tools": self._convert_tools(TOOL_DEFINITIONS),
            "stream": True
        }

        async with self.client.stream("POST", f"{self.url}/chat/completions", json=payload) as response:
            if response.status_code != 200:
                error_body = await response.aread()
                raise Exception(f"Hermes API error {response.status_code}: {error_body.decode()}")

            current_thought = ""
            in_thought = False
            
            async for line in response.aiter_lines():
                if not line.startswith("data: "):
                    continue
                
                data_str = line[6:].strip()
                if data_str == "[DONE]":
                    break
                
                try:
                    chunk = json.loads(data_str)
                    delta = chunk["choices"][0]["delta"]
                    
                    # Handle tool calls (if any in this delta)
                    if "tool_calls" in delta:
                        # For now, we return the tool_calls in a pseudo-event handled by the caller
                        yield {"type": "tool_calls", "content": delta["tool_calls"]}
                        continue

                    # Handle text and reasoning
                    content = delta.get("content", "")
                    if not content:
                        continue

                    # Parse reasoning tags: <thought> or <scratch_pad>
                    # This is a simple streaming parser for tags
                    while content:
                        if not in_thought:
                            if "<thought>" in content or "<scratch_pad>" in content:
                                tag = "<thought>" if "<thought>" in content else "<scratch_pad>"
                                before, after = content.split(tag, 1)
                                if before:
                                    yield {"type": "text", "content": before}
                                yield {"type": "thinking_start"}
                                in_thought = True
                                content = after
                            else:
                                yield {"type": "text", "content": content}
                                content = ""
                        else:
                            end_tag = "</thought>" if "</thought>" in content else "</scratch_pad>"
                            if end_tag in content:
                                thought_part, after = content.split(end_tag, 1)
                                if thought_part:
                                    yield {"type": "thinking_delta", "content": thought_part}
                                # We don't have a thinking_stop in the UI, so we just toggle back to text
                                in_thought = False
                                content = after
                            else:
                                yield {"type": "thinking_delta", "content": content}
                                content = ""
                                
                except Exception as e:
                    print(f"Error parsing Hermes chunk: {e}")
                    continue

    async def get_final_metrics(self):
        # Hermes Agent usually doesn't return usage in streaming choice chunks yet 
        # unless it's in the final [DONE] or a separate message.
        return 0, 0, 0.0

    async def close(self):
        await self.client.aclose()


async def stream_chat(
    history: list[dict],
    user_message: str,
    model: str = "claude-sonnet-4-5",
) -> AsyncGenerator[str, None]:
    """
    Runs the agentic loop and yields SSE-formatted strings.
    history: list of prior {role, content} dicts
    user_message: the new user input
    model: the model/provider ID to use
    """
    messages = history + [{"role": "user", "content": user_message}]

    # Yield an initial space or newline to "prime" the stream and flush buffers.
    yield ":" + " " * 4096 + "\n\n"

    try:
        if model in ("hermes-agent", "hermes-remote"):
            # --- Hermes Agent Loop ---
            if model == "hermes-remote":
                provider = HermesProvider(url=HERMES_REMOTE_URL, api_key=HERMES_REMOTE_API_KEY)
            else:
                provider = HermesProvider(url=HERMES_URL, api_key=HERMES_API_KEY)
            turn_count = 0
            while True:
                turn_count += 1
                if turn_count > 1:
                    yield _sse({"type": "status", "text": "Verarbeite Zwischenergebnisse…"})
                
                assistant_text_in_turn = ""
                tool_calls_in_turn = {} # index -> {name, input_json}
                
                async for event in provider.chat_stream(messages, SYSTEM_PROMPT):
                    if event["type"] == "text":
                        assistant_text_in_turn += event["content"]
                        yield _sse({"type": "text", "content": event["content"]})
                    elif event["type"] == "thinking_start":
                        yield _sse({"type": "thinking_start", "index": 0})
                    elif event["type"] == "thinking_delta":
                        yield _sse({"type": "thinking_delta", "index": 0, "delta": event["content"]})
                    elif event["type"] == "tool_calls":
                        for tc in event["content"]:
                            idx = tc.get("index", 0)
                            if idx not in tool_calls_in_turn:
                                tool_calls_in_turn[idx] = {"name": "", "arguments": ""}
                            
                            if "function" in tc:
                                if "name" in tc["function"] and tc["function"]["name"]:
                                    tool_calls_in_turn[idx]["name"] = tc["function"]["name"]
                                    yield _sse({"type": "tool_start", "name": tc["function"]["name"], "index": idx})
                                if "arguments" in tc["function"]:
                                    tool_calls_in_turn[idx]["arguments"] += tc["function"]["arguments"]
                                    yield _sse({"type": "tool_input_delta", "index": idx, "delta": tc["function"]["arguments"]})

                # Append assistant turn to history
                # We also need to include the tool_calls in the assistant message for the next turn
                assistant_msg = {"role": "assistant", "content": assistant_text_in_turn}
                if tool_calls_in_turn:
                    assistant_msg["tool_calls"] = [
                        {
                            "id": f"hermes_{idx}_{tc_data['name']}",
                            "type": "function",
                            "function": {
                                "name": tc_data["name"],
                                "arguments": tc_data["arguments"]
                            }
                        }
                        for idx, tc_data in tool_calls_in_turn.items()
                    ]
                messages.append(assistant_msg)

                if not tool_calls_in_turn:
                    break

                # Execute requested tools
                for idx, tc_data in tool_calls_in_turn.items():
                    name = tc_data["name"]
                    raw_args = tc_data["arguments"]
                    try:
                        args = json.loads(raw_args) if raw_args else {}
                    except:
                        args = {"raw": raw_args}
                    
                    result_text = await execute_tool(name, args)
                    yield _sse({
                        "type": "tool_done",
                        "index": idx,
                        "name": name,
                        "input": args,
                        "result": result_text
                    })

                    messages.append({
                        "role": "tool",
                        "tool_call_id": f"hermes_{idx}_{name}",
                        "name": name,
                        "content": result_text,
                    })

            await provider.close()
            yield _sse({"type": "done", "tokens_input": 0, "tokens_output": 0, "cost_usd": 0.0})

        else:
            # --- Claude / Anthropic Loop ---
            client = anthropic.AsyncAnthropic()
            INPUT_COST_PER_M = 3.0
            OUTPUT_COST_PER_M = 15.0
            total_input_tokens = 0
            total_output_tokens = 0

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
                        model=model,
                        max_tokens=8192,
                        system=SYSTEM_PROMPT,
                        thinking={"type": "enabled", "budget_tokens": 4096},
                        tools=TOOL_DEFINITIONS + [code_execution_tool],
                        messages=messages,
                        betas=["skills-2025-10-02", "code-execution-2025-08-25"],
                        container={"skills": [{"type": "custom", "skill_id": sid, "version": "latest"} for sid in skill_ids]},
                    )
                else:
                    stream_cm = client.messages.stream(
                        model=model,
                        max_tokens=8192,
                        system=SYSTEM_PROMPT,
                        tools=TOOL_DEFINITIONS,
                        messages=messages,
                        thinking={"type": "enabled", "budget_tokens": 4096},
                    )
                
                async with stream_cm as stream:
                    server_tool_id_to_index: dict[str, int] = {}
                    result_to_skill: dict[int, int] = {}
                    code_exec_buffer: dict[int, str] = {}
                    active_skill_indices: set[int] = set()

                    async for event in stream:
                        if event.type == "content_block_start":
                            block_type = getattr(event.content_block, "type", "")
                            block_name = getattr(event.content_block, "name", "")
                            block_id   = getattr(event.content_block, "id", "")
                            tool_use_id = getattr(event.content_block, "tool_use_id", "")

                            if block_type in ("server_tool_use", "tool_use") and block_name == "code_execution":
                                code_exec_buffer[event.index] = ""
                                if block_id: server_tool_id_to_index[block_id] = event.index
                                active_skill_indices.add(event.index)
                                yield _sse({"type": "skill_event", "action": "start", "index": event.index, "skills": skill_names, "files": []})
                            elif block_type in ("server_tool_use", "tool_use"):
                                yield _sse({"type": "tool_start", "name": block_name, "index": event.index})
                            elif block_type == "thinking":
                                yield _sse({"type": "thinking_start", "index": event.index})
                            elif block_type == "bash_code_execution_tool_result":
                                skill_idx = server_tool_id_to_index.get(tool_use_id, None)
                                if skill_idx is not None: result_to_skill[event.index] = skill_idx

                        elif event.type == "content_block_delta":
                            if event.delta.type == "text_delta":
                                yield _sse({"type": "text", "content": event.delta.text})
                            elif event.index in code_exec_buffer:
                                code_exec_buffer[event.index] += getattr(event.delta, "partial_json", "")
                            elif event.delta.type == "input_json_delta":
                                yield _sse({"type": "tool_input_delta", "index": event.index, "delta": getattr(event.delta, "partial_json", "")})
                            elif event.delta.type == "thinking_delta":
                                yield _sse({"type": "thinking_delta", "index": event.index, "delta": getattr(event.delta, "thinking", "")})

                        elif event.type == "content_block_stop":
                            if event.index in result_to_skill:
                                skill_idx = result_to_skill.pop(event.index)
                                code = code_exec_buffer.pop(skill_idx, "")
                                matches = re.findall(r"/skills/([^/'\"\\\s]+)/([^'\"\)\\\s]+)", code)
                                files = [f"{s}/{f}" for s, f in matches]
                                active_skill_indices.discard(skill_idx)
                                yield _sse({"type": "skill_event", "action": "done", "index": skill_idx, "files": files})
                            elif event.index in active_skill_indices:
                                if event.index not in server_tool_id_to_index.values():
                                    active_skill_indices.discard(event.index)
                                    code_exec_buffer.pop(event.index, None)
                                    yield _sse({"type": "skill_event", "action": "done", "index": event.index})
                            else:
                                code_exec_buffer.pop(event.index, None)

                    final = await stream.get_final_message()

                total_input_tokens += final.usage.input_tokens
                total_output_tokens += final.usage.output_tokens
                messages.append({"role": "assistant", "content": final.content})

                if final.stop_reason != "tool_use":
                    break

                tool_results = []
                for idx, block in enumerate(final.content):
                    if block.type != "tool_use": continue
                    result_text = await execute_tool(block.name, block.input)
                    yield _sse({"type": "tool_done", "index": idx, "name": block.name, "input": block.input, "result": result_text})
                    tool_results.append({"type": "tool_result", "tool_use_id": block.id, "content": result_text})
                messages.append({"role": "user", "content": tool_results})

            cost_usd = (total_input_tokens * INPUT_COST_PER_M + total_output_tokens * OUTPUT_COST_PER_M) / 1_000_000
            yield _sse({"type": "cost", "input_tokens": total_input_tokens, "output_tokens": total_output_tokens, "cost_usd": round(cost_usd, 6)})
            yield _sse({"type": "done", "tokens_input": total_input_tokens, "tokens_output": total_output_tokens, "cost_usd": cost_usd})

    except Exception as e:
        yield _sse({"type": "error", "content": str(e)})


def _sse(payload: dict) -> str:
    return f"data: {json.dumps(payload, ensure_ascii=False)}\n\n"
