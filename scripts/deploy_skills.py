"""
Lädt alle Skills aus dem skills/-Ordner zur Anthropic Skills API hoch.

Jeder Unterordner in skills/ wird als Skill hochgeladen.
Bestehende Skills werden aktualisiert, neue erstellt, entfernte gelöscht.
Die resultierenden Skill-IDs werden in skill_ids.json gespeichert.

Verwendung:
    python3 scripts/deploy_skills.py
"""
import json
import os
import sys
from pathlib import Path

import anthropic

SKILLS_DIR = Path("skills")
SKILL_IDS_FILE = Path("skill_ids.json")
BETAS = ["skills-2025-10-02"]


def files_from_dir(skill_dir: Path) -> list:
    """Gibt alle Dateien eines Skill-Verzeichnisses als (name, bytes, mime)-Tuples zurück.
    Pfade werden mit dem Verzeichnisnamen als Prefix versehen (z.B. 'mein-skill/SKILL.md'),
    wie von der API gefordert ('common root directory')."""
    prefix = skill_dir.name
    return [
        (f"{prefix}/{f.relative_to(skill_dir)}", f.read_bytes(), "text/plain")
        for f in sorted(skill_dir.rglob("*"))
        if f.is_file()
    ]


def load_skill_ids() -> dict:
    try:
        return json.loads(SKILL_IDS_FILE.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_skill_ids(ids: dict) -> None:
    SKILL_IDS_FILE.write_text(json.dumps(ids, indent=2, ensure_ascii=False) + "\n")


def main() -> None:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        sys.exit("ERROR: ANTHROPIC_API_KEY nicht gesetzt")

    client = anthropic.Anthropic(api_key=api_key)
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
                # Zuerst alle Versionen löschen, dann den Skill
                versions = client.beta.skills.versions.list(skill_id, betas=BETAS)
                for v in versions.data:
                    client.beta.skills.versions.delete(v.version, skill_id=skill_id, betas=BETAS)
                client.beta.skills.delete(skill_id, betas=BETAS)
                print(f"    Gelöscht.")
            except anthropic.NotFoundError:
                print(f"    War bereits gelöscht.")
            except anthropic.APIStatusError as e:
                print(f"    FEHLER beim Löschen: {e.status_code} – {e.message}")
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

        existing_id = ids.get(name)
        try:
            if existing_id:
                # Neue Version hochladen (= Update des Skills)
                client.beta.skills.versions.create(
                    existing_id,
                    files=files_from_dir(skill_dir),
                    betas=BETAS,
                )
                print(f"    Aktualisiert: {existing_id}")
                ids[name] = existing_id
            else:
                skill = client.beta.skills.create(
                    display_title=name,
                    files=files_from_dir(skill_dir),
                    betas=BETAS,
                )
                print(f"    Erstellt:     {skill.id}")
                ids[name] = skill.id
        except anthropic.NotFoundError:
            # ID in skill_ids.json existiert nicht mehr bei Anthropic → neu anlegen
            print(f"    Skill-ID ungültig, erstelle neu...")
            skill = client.beta.skills.create(
                display_title=name,
                files=files_from_dir(skill_dir),
                betas=BETAS,
            )
            print(f"    Erstellt:     {skill.id}")
            ids[name] = skill.id
        except anthropic.APIStatusError as e:
            print(f"    FEHLER: {e.status_code} – {e.message}")
            sys.exit(1)

    save_skill_ids(ids)
    print(f"  skill_ids.json aktualisiert ({len(ids)} Skills).")


if __name__ == "__main__":
    print("--- Skills zur Anthropic API hochladen ---")
    main()
