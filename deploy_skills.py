"""
Lädt alle Skills aus dem skills/-Ordner zur Anthropic Skills API hoch.

Jeder Unterordner in skills/ wird zu einem ZIP-Archiv und als Skill
hochgeladen. Bestehende Skills werden aktualisiert (PUT), neue erstellt (POST).
Die resultierenden Skill-IDs werden in skill_ids.json gespeichert.

Verwendung:
    python deploy_skills.py
"""
import io
import json
import os
import sys
import zipfile
from pathlib import Path

import httpx

SKILLS_DIR = Path("skills")
SKILL_IDS_FILE = Path("skill_ids.json")
API_BASE = "https://api.anthropic.com/v1"
ANTHROPIC_VERSION = "2023-06-01"


def build_zip(skill_dir: Path) -> bytes:
    """Packt den Inhalt eines Skill-Verzeichnisses in ein ZIP."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in sorted(skill_dir.rglob("*")):
            if file.is_file():
                zf.write(file, file.relative_to(skill_dir))
    return buf.getvalue()


def load_skill_ids() -> dict:
    try:
        return json.loads(SKILL_IDS_FILE.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_skill_ids(ids: dict) -> None:
    SKILL_IDS_FILE.write_text(json.dumps(ids, indent=2, ensure_ascii=False) + "\n")


def get_headers(api_key: str) -> dict:
    return {
        "x-api-key": api_key,
        "anthropic-version": ANTHROPIC_VERSION,
    }


def create_skill(api_key: str, zip_bytes: bytes) -> str:
    """Erstellt einen neuen Skill und gibt die ID zurück."""
    resp = httpx.post(
        f"{API_BASE}/skills",
        headers=get_headers(api_key),
        files={"file": ("skill.zip", zip_bytes, "application/zip")},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()["id"]


def update_skill(api_key: str, skill_id: str, zip_bytes: bytes) -> str:
    """Aktualisiert einen bestehenden Skill und gibt die ID zurück."""
    resp = httpx.put(
        f"{API_BASE}/skills/{skill_id}",
        headers=get_headers(api_key),
        files={"file": ("skill.zip", zip_bytes, "application/zip")},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()["id"]


def delete_skill(api_key: str, skill_id: str) -> None:
    """Löscht einen Skill bei Anthropic."""
    resp = httpx.delete(
        f"{API_BASE}/skills/{skill_id}",
        headers=get_headers(api_key),
        timeout=60,
    )
    resp.raise_for_status()


def main() -> None:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        sys.exit("ERROR: ANTHROPIC_API_KEY nicht gesetzt")

    ids = load_skill_ids()

    # Gelöschte Skills entfernen (in skill_ids.json vorhanden, aber kein Ordner mehr)
    existing_dirs = (
        {d.name for d in SKILLS_DIR.iterdir() if d.is_dir()}
        if SKILLS_DIR.exists()
        else set()
    )
    for name in list(ids.keys()):
        if name not in existing_dirs:
            skill_id = ids[name]
            print(f"  → Lösche Skill: {name} ({skill_id})")
            try:
                delete_skill(api_key, skill_id)
                print(f"    Gelöscht.")
            except httpx.HTTPStatusError as e:
                print(f"    FEHLER beim Löschen: {e.response.status_code} – {e.response.text}")
                sys.exit(1)
            del ids[name]

    if not SKILLS_DIR.exists():
        print("Kein skills/-Ordner gefunden – überspringe Skill-Upload.")
        save_skill_ids(ids)
        return

    skill_dirs = [d for d in sorted(SKILLS_DIR.iterdir()) if d.is_dir()]
    if not skill_dirs:
        print("Keine Skills gefunden – überspringe Skill-Upload.")
        save_skill_ids(ids)
        return

    # Neue und geänderte Skills hochladen
    for skill_dir in skill_dirs:
        name = skill_dir.name
        print(f"  → Verarbeite Skill: {name}")

        zip_bytes = build_zip(skill_dir)

        existing_id = ids.get(name)
        try:
            if existing_id:
                skill_id = update_skill(api_key, existing_id, zip_bytes)
                print(f"    Aktualisiert: {skill_id}")
            else:
                skill_id = create_skill(api_key, zip_bytes)
                print(f"    Erstellt:     {skill_id}")
            ids[name] = skill_id
        except httpx.HTTPStatusError as e:
            print(f"    FEHLER: {e.response.status_code} – {e.response.text}")
            sys.exit(1)

    save_skill_ids(ids)
    print(f"  skill_ids.json aktualisiert ({len(ids)} Skills).")


if __name__ == "__main__":
    print("--- Skills zur Anthropic API hochladen ---")
    main()
