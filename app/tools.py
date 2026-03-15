"""
Tool implementations for Claude's agentic loop.

Two tools:
  1. search_local_cases  – SQLite FTS5 search on local Präjudizen DB
  2. search_opencaselaw  – Remote MCP call to https://mcp.opencaselaw.ch
"""
import json
import sqlite3
from mcp import ClientSession
from mcp.client.sse import sse_client

from app.database import DB_PATH

# ---------------------------------------------------------------------------
# Tool definitions (JSON schema) passed to Claude
# ---------------------------------------------------------------------------

TOOL_DEFINITIONS = [
    {
        "name": "search_local_cases",
        "description": (
            "Searches the local database of Präjudizen (internal court decisions). "
            "Use this first to check whether a relevant precedent already exists in our records. "
            "Returns Titel and Regeste of matching cases."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Keywords to search for, e.g. 'Betrug Arglist Zivilklage'",
                },
                "limit": {
                    "type": "integer",
                    "description": "Max number of results (default 5)",
                    "default": 5,
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "search_opencaselaw",
        "description": (
            "Searches public Swiss court decisions via OpenCaseLaw (956,000+ decisions). "
            "Use this to find leading cases, BGE decisions, or cantonal rulings on a topic. "
            "Returns case summaries with citation and court information."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Legal search query in German or French",
                },
                "limit": {
                    "type": "integer",
                    "description": "Max number of results (default 5)",
                    "default": 5,
                },
            },
            "required": ["query"],
        },
    },
]


# ---------------------------------------------------------------------------
# Tool 1: Local DB search
# ---------------------------------------------------------------------------

def search_local_cases(query: str, limit: int = 5) -> str:
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row

        # FTS5 MATCH with snippet for urteilsauszug context
        rows = conn.execute(
            """
            SELECT p.titel,
                   p.regeste,
                   snippet(praejudizen_fts, 2, '<<', '>>', '...', 15) AS excerpt
            FROM praejudizen_fts fts
            JOIN praejudizen p ON p.id = fts.rowid
            WHERE praejudizen_fts MATCH ?
            ORDER BY rank
            LIMIT ?
            """,
            (query, limit),
        ).fetchall()
        conn.close()

        if not rows:
            return f"Keine Präjudizen gefunden für: '{query}'"

        parts = []
        for row in rows:
            parts.append(
                f"**{row['titel']}**\n"
                f"Regeste: {row['regeste']}\n"
                f"Auszug: {row['excerpt']}"
            )
        return f"Gefundene Präjudizen ({len(rows)}):\n\n" + "\n\n---\n\n".join(parts)

    except Exception as e:
        return f"Fehler bei der Datenbanksuche: {e}"


# ---------------------------------------------------------------------------
# Tool 2: OpenCaseLaw MCP search
# ---------------------------------------------------------------------------

MCP_SERVER_URL = "https://mcp.opencaselaw.ch"


async def search_opencaselaw(query: str, limit: int = 5) -> str:
    try:
        async with sse_client(MCP_SERVER_URL) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool(
                    "search_decisions",
                    {"query": query, "limit": limit},
                )

        # result.content is a list of TextContent / ImageContent
        parts = []
        for block in result.content:
            if hasattr(block, "text"):
                parts.append(block.text)

        if not parts:
            return f"Keine Entscheide gefunden für: '{query}'"

        return "\n\n".join(parts)

    except Exception as e:
        return f"Fehler bei OpenCaseLaw: {e}"


# ---------------------------------------------------------------------------
# Dispatcher: route tool_use block to the right implementation
# ---------------------------------------------------------------------------

async def execute_tool(name: str, tool_input: dict) -> str:
    if name == "search_local_cases":
        return search_local_cases(
            query=tool_input["query"],
            limit=tool_input.get("limit", 5),
        )
    elif name == "search_opencaselaw":
        return await search_opencaselaw(
            query=tool_input["query"],
            limit=tool_input.get("limit", 5),
        )
    else:
        return f"Unbekanntes Tool: {name}"
