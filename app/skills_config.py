"""Liest die Skill-IDs aus skill_ids.json für den API-Call."""
import json
from pathlib import Path
from typing import Optional

_SKILL_IDS_PATH = Path(__file__).parent.parent / "skill_ids.json"


def get_skill_ids() -> list[str]:
    """Gibt alle Skill-IDs zurück. Leere Liste wenn Datei fehlt oder leer ist."""
    try:
        data = json.loads(_SKILL_IDS_PATH.read_text())
        return list(data.values())
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def get_skill_names() -> list[str]:
    """Gibt alle Skill-Ordnernamen zurück (entspricht dem skill name in SKILL.md)."""
    try:
        data = json.loads(_SKILL_IDS_PATH.read_text())
        return list(data.keys())
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def get_skill_id(name: str) -> Optional[str]:
    """Gibt die ID eines bestimmten Skills zurück."""
    try:
        data = json.loads(_SKILL_IDS_PATH.read_text())
        return data.get(name)
    except (FileNotFoundError, json.JSONDecodeError):
        return None
