"""
Tool implementations for Claude's agentic loop.

Sources:
  1. search_local_cases   – SQLite FTS5 search on local Präjudizen DB
  2. OpenCaseLaw (MCP)    – 12 tools via https://mcp.opencaselaw.ch
       search_decisions, find_leading_cases, get_decision, get_case_brief,
       find_citations, find_appeal_chain, get_law, search_laws,
       get_commentary, search_commentaries, get_doctrine, analyze_legal_trend
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
    # ------------------------------------------------------------------
    # Local DB
    # ------------------------------------------------------------------
    {
        "name": "search_local_cases",
        "description": (
            "Durchsucht die lokale Datenbank der internen Präjudizen des Kriminalgerichts Luzern. "
            "Immer zuerst aufrufen, bevor öffentliche Quellen konsultiert werden. "
            "Gibt Titel, Regeste und Urteilsauszug zurück."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Suchbegriffe, z.B. 'Betrug Arglist Zivilklage'",
                },
                "limit": {
                    "type": "integer",
                    "description": "Max. Anzahl Treffer (Standard 5)",
                    "default": 5,
                },
            },
            "required": ["query"],
        },
    },

    # ------------------------------------------------------------------
    # OpenCaseLaw – Entscheide
    # ------------------------------------------------------------------
    {
        "name": "search_decisions",
        "description": (
            "Volltextsuche in 956'000+ öffentlichen Schweizer Gerichtsentscheiden. "
            "Unterstützt Keywords, Phrasen (in Anführungszeichen), Boolesche Operatoren (AND, OR, NOT), "
            "Geschäftsnummern (z.B. 6B_1234/2025) und Spaltenfilter (regeste:..., full_text:...). "
            "Filterbar nach Gericht, Kanton, Sprache, Datum, Kammer und Entscheidtyp."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Suchanfrage, z.B. 'Betrug AND Arglist' oder '\"ungetreue Geschäftsbesorgung\"'",
                },
                "court": {
                    "type": "string",
                    "description": "Gericht: bger, bge, bvger, bstger oder kantonale Codes wie zh_obergericht",
                },
                "canton": {"type": "string", "description": "Kanton: CH, ZH, BE, LU, GE usw."},
                "date_from": {"type": "string", "description": "Von Datum (YYYY-MM-DD)"},
                "date_to": {"type": "string", "description": "Bis Datum (YYYY-MM-DD)"},
                "language": {"type": "string", "enum": ["de", "fr", "it", "rm"]},
                "decision_type": {"type": "string", "description": "z.B. 'Urteil', 'Beschluss', 'Leitentscheid'"},
                "sort": {"type": "string", "enum": ["relevance", "date_desc", "date_asc"]},
                "limit": {"type": "integer", "default": 10},
                "offset": {"type": "integer", "default": 0},
            },
            "required": ["query"],
        },
    },
    {
        "name": "find_leading_cases",
        "description": (
            "Findet die meistzitierten Leitentscheide zu einem Thema oder Gesetzesartikel. "
            "Ranking basiert auf dem Zitationsgraphen (8,77 Mio. Kanten). "
            "Filterbar nach Gesetz/Artikel (z.B. StGB Art. 146), Thema, Gericht und Datum."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Thema, z.B. 'Betrug Arglist'"},
                "law_code": {"type": "string", "description": "Gesetzes-Kürzel, z.B. StGB, BV, OR"},
                "article": {"type": "string", "description": "Artikelnummer (benötigt law_code)"},
                "court": {"type": "string", "description": "z.B. bger, bge"},
                "date_from": {"type": "string", "description": "Von Datum (YYYY-MM-DD)"},
                "date_to": {"type": "string", "description": "Bis Datum (YYYY-MM-DD)"},
                "limit": {"type": "integer", "default": 10},
            },
            "required": [],
        },
    },
    {
        "name": "get_decision",
        "description": (
            "Ruft einen einzelnen Gerichtsentscheid mit vollem Text ab. "
            "Akzeptiert decision_id (z.B. bger_6B_1234_2025), Geschäftsnummer (6B_1234/2025) "
            "oder BGE-Referenz. Volltext wird bei sehr langen Entscheiden auf 200'000 Zeichen begrenzt."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "decision_id": {
                    "type": "string",
                    "description": "Decision-ID, Geschäftsnummer oder BGE-Referenz",
                },
                "full_text": {
                    "type": "boolean",
                    "default": True,
                    "description": "Volltext einschliessen (Standard true). False für nur Metadaten/Regeste.",
                },
            },
            "required": ["decision_id"],
        },
    },
    {
        "name": "get_case_brief",
        "description": (
            "Erstellt ein strukturiertes Case Brief für einen Schweizer Gerichtsentscheid. "
            "Gibt Regeste, Sachverhalt, Erwägungen (mit Absatznummern), Dispositiv, "
            "anwendbare Gesetzesartikel, Zitationsautorität und verwandte Entscheide zurück."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "case": {
                    "type": "string",
                    "description": "BGE-Referenz ('BGE 133 III 121'), decision_id oder Geschäftsnummer",
                },
            },
            "required": ["case"],
        },
    },
    {
        "name": "find_citations",
        "description": (
            "Zeigt, welche Entscheide ein bestimmter Entscheid zitiert und welche ihn zitieren. "
            "Nutzt den Referenzgraphen mit 8,77 Mio. Kanten. "
            "Gibt aufgelöste Zitationen mit Konfidenzwerten zurück."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "decision_id": {"type": "string", "description": "Decision-ID, z.B. bger_6B_1_2025"},
                "direction": {
                    "type": "string",
                    "enum": ["both", "outgoing", "incoming"],
                    "default": "both",
                    "description": "both = zitiert + wird zitiert von",
                },
                "limit": {"type": "integer", "default": 20},
            },
            "required": ["decision_id"],
        },
    },
    {
        "name": "find_appeal_chain",
        "description": (
            "Verfolgt den Instanzenzug eines Entscheids. "
            "Zeigt Vorinstanzen und nachfolgende Instanzen, z.B. Bezirksgericht → Obergericht → Bundesgericht."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "decision_id": {"type": "string", "description": "Decision-ID, z.B. bger_6B_1_2025"},
            },
            "required": ["decision_id"],
        },
    },

    # ------------------------------------------------------------------
    # OpenCaseLaw – Gesetze
    # ------------------------------------------------------------------
    {
        "name": "get_law",
        "description": (
            "Ruft einen Schweizer Bundesgesetzesartikel oder die Artikelübersicht ab. "
            "Zugriff über SR-Nummer oder Kürzel (BV, OR, ZGB, StGB, StPO usw.). "
            "Beispiele: get_law(abbreviation='StGB', article='146') für Art. 146 StGB."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "abbreviation": {"type": "string", "description": "Gesetzes-Kürzel, z.B. StGB, StPO, BV"},
                "sr_number": {"type": "string", "description": "SR-Nummer, z.B. '311.0' für StGB"},
                "article": {"type": "string", "description": "Artikelnummer, z.B. '146'. Ohne Angabe: Artikelübersicht."},
                "language": {"type": "string", "enum": ["de", "fr", "it"], "default": "de"},
            },
            "required": [],
        },
    },
    {
        "name": "search_laws",
        "description": (
            "Volltextsuche in allen Schweizer Bundesgesetzesartikeln. "
            "Nützlich um herauszufinden, welche Artikel ein bestimmtes Thema behandeln. "
            "Beispiel: 'Verjährung Strafrecht' oder 'Notwehr'."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Suchanfrage, z.B. 'Verjährung' oder 'Notwehr'"},
                "sr_number": {"type": "string", "description": "Suche auf ein bestimmtes Gesetz einschränken"},
                "language": {"type": "string", "enum": ["de", "fr", "it"], "default": "de"},
                "limit": {"type": "integer", "default": 10},
            },
            "required": ["query"],
        },
    },

    # ------------------------------------------------------------------
    # OpenCaseLaw – Doktrin & Kommentare
    # ------------------------------------------------------------------
    {
        "name": "get_doctrine",
        "description": (
            "Gibt die Leitentscheide und Dogmatik zu einem Gesetzesartikel oder Rechtsbegriff zurück. "
            "Eingabe: Gesetzesartikel ('Art. 146 StGB') oder Rechtsbegriff ('Arglist', 'Notwehr', 'Gehilfenschaft'). "
            "Gibt Gesetzestext, Top-BGEs nach Zitationsautorität, die jeweilige Regel aus der Regeste "
            "und eine Dogmatik-Zeitleiste zurück."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Gesetzesartikel ('Art. 146 StGB') oder Rechtsbegriff ('Arglist')",
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "get_commentary",
        "description": (
            "Ruft den wissenschaftlichen Kommentar von OnlineKommentar.ch (CC-BY-4.0) "
            "für einen Schweizer Bundesgesetzesartikel ab. "
            "Deckt StGB, StPO, BV, OR, ZGB, ZPO, DSG, SchKG u.a. ab. "
            "Ohne Artikel: Liste der kommentierten Artikel. Mit Artikel: Volltext des Kommentars."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "abbreviation": {"type": "string", "description": "Gesetzes-Kürzel, z.B. StGB, StPO"},
                "article": {"type": "string", "description": "Artikelnummer, z.B. '146'. Ohne Angabe: Artikelübersicht."},
                "language": {"type": "string", "enum": ["de", "fr", "it", "en"], "default": "de"},
            },
            "required": [],
        },
    },
    {
        "name": "search_commentaries",
        "description": (
            "Volltextsuche in allen OnlineKommentar.ch-Kommentaren. "
            "Nützlich für die Doktrin zu einem Rechtsbegriff über mehrere Gesetze hinweg. "
            "Beispiel: 'Arglist' oder 'direkter Vorsatz'."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Suchanfrage"},
                "abbreviation": {"type": "string", "description": "Filter auf ein Gesetz, z.B. StGB"},
                "language": {"type": "string", "description": "de, fr, it, en"},
                "limit": {"type": "integer", "default": 10},
            },
            "required": ["query"],
        },
    },

    # ------------------------------------------------------------------
    # OpenCaseLaw – Trends
    # ------------------------------------------------------------------
    {
        "name": "analyze_legal_trend",
        "description": (
            "Zeigt die jährliche Entwicklung der Rechtsprechung zu einem Thema oder Gesetzesartikel. "
            "Gibt Entscheidszahlen pro Jahr mit Balkendiagramm zurück. "
            "Nützlich um zu sehen, ob ein Thema an Bedeutung gewonnen oder verloren hat."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Thema, z.B. 'Betrug' oder 'Notwehr'"},
                "law_code": {"type": "string", "description": "Gesetzes-Kürzel (benötigt article)"},
                "article": {"type": "string", "description": "Artikelnummer (benötigt law_code)"},
                "court": {"type": "string", "description": "Gerichtsfilter"},
                "date_from": {"type": "string"},
                "date_to": {"type": "string"},
            },
            "required": [],
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

        rows = conn.execute(
            """
            SELECT p.titel,
                   p.regeste,
                   p.urteilsauszug
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
                f"Urteilsauszug: {row['urteilsauszug']}"
            )
        return f"Gefundene Präjudizen ({len(rows)}):\n\n" + "\n\n---\n\n".join(parts)

    except Exception as e:
        return f"Fehler bei der Datenbanksuche: {e}"


# ---------------------------------------------------------------------------
# Tool 2–13: OpenCaseLaw MCP – generic dispatcher
# ---------------------------------------------------------------------------

MCP_SERVER_URL = "https://mcp.opencaselaw.ch"

# All tool names that are routed to the OpenCaseLaw MCP server
OPENCASELAW_TOOLS = {
    "search_decisions",
    "find_leading_cases",
    "get_decision",
    "get_case_brief",
    "find_citations",
    "find_appeal_chain",
    "get_law",
    "search_laws",
    "get_doctrine",
    "get_commentary",
    "search_commentaries",
    "analyze_legal_trend",
}


async def call_opencaselaw(tool_name: str, params: dict) -> str:
    try:
        async with sse_client(MCP_SERVER_URL) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool(tool_name, params)

        parts = [block.text for block in result.content if hasattr(block, "text")]
        return "\n\n".join(parts) if parts else f"Keine Ergebnisse von '{tool_name}'."

    except Exception as e:
        return f"Fehler bei OpenCaseLaw ({tool_name}): {e}"


# ---------------------------------------------------------------------------
# Dispatcher: route tool_use block to the right implementation
# ---------------------------------------------------------------------------

async def execute_tool(name: str, tool_input: dict) -> str:
    if name == "search_local_cases":
        return search_local_cases(
            query=tool_input["query"],
            limit=tool_input.get("limit", 5),
        )
    elif name in OPENCASELAW_TOOLS:
        return await call_opencaselaw(name, tool_input)
    else:
        return f"Unbekanntes Tool: {name}"
