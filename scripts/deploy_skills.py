"""
Lädt alle Skills aus dem skills/-Ordner zur Anthropic Skills API hoch.

Jeder Unterordner in skills/ wird als Skill hochgeladen.
Bestehende Skills werden aktualisiert, neue erstellt, entfernte gelöscht.
Die resultierenden Skill-IDs werden in skill_ids.json gespeichert.

Verwendung:
    python3 scripts/deploy_skills.py
"""
import io
import json
import os
import re
import sys
import tarfile
import unicodedata
from pathlib import Path

import anthropic

TENANT = os.environ.get("TENANT", "krg")
SKILLS_DIR = Path("skills") / TENANT
SKILL_IDS_FILE = SKILLS_DIR / "skill_ids.json"
BETAS = ["skills-2025-10-02"]



# .gz: gzip-komprimierter Volltext der Originalquellen (resources/quellen/)
VALID_EXTENSIONS = {".md", ".txt", ".json", ".csv", ".gz"}

# Harte Grenzen der Anthropic Skills API (empirisch ermittelt):
#   - Max. 200 Dateien pro Skill ("Skill contains too many files").
#   - Max. 30 MB pro Skill insgesamt.
#   - Pfade nur aus [A-Za-z0-9._/-]; Leerzeichen/Umlaute/Klammern -> 400
#     "path with invalid characters". (Ein ZIP würde beliebige Namen erlauben,
#     ist aber pro Part gedeckelt und kann nicht geschachtelt/gestückelt
#     werden -> für >1 MB unbrauchbar. Daher Einzeldatei-Upload.)
#   - Pro Part nennt die API 1024 KB, real scheitern Parts ab ~900 KB
#     sporadisch mit 400/502. Parts <= ~250 KB laden zuverlässig, auch wenn
#     der Gesamt-Body mehrere MB beträgt (getestet: 140 Dateien / 4.9 MB).
# Die Volltext-Quellen (resources/quellen/, ~227 Dateien mit Leerzeichen/Umlauten
# im Namen) sprengen sowohl die Datei-Anzahl als auch den Zeichensatz. Sie werden
# deshalb beim Deploy in viele kleine tar.gz-Bündel gepackt; der Skill entpackt
# sie zur Laufzeit (siehe SKILL.md). Die Originalnamen bleiben IM tar erhalten
# (für zgrep und SharePoint-Links).
MAX_FILES = 200
MAX_PART_BYTES = 1024 * 1024
MAX_SKILL_BYTES = 30 * 1024 * 1024
BUNDLE_TARGET_BYTES = 240 * 1024  # kleine Parts laden zuverlässig (s.o.)
SAFE_PATH = re.compile(r"^[A-Za-z0-9._/-]+$")


def _bundle_quellen(quellen_dir: Path, prefix: str) -> list:
    """Packt resources/quellen/** in tar.gz-Bündel <1024 KB.
    Rückgabe: Liste von (arc_name, bytes)-Tupeln. Pfade im tar sind relativ zu
    quellen_dir, sodass das Entpacken die Struktur Literatur/TBS/... wiederherstellt."""
    src = sorted(f for f in quellen_dir.rglob("*") if f.is_file() and f.suffix.lower() in VALID_EXTENSIONS)
    bundles, batch, batch_bytes = [], [], 0

    def flush(idx, files):
        buf = io.BytesIO()
        with tarfile.open(fileobj=buf, mode="w:gz") as tar:
            for f in files:
                tar.add(f, arcname=f.relative_to(quellen_dir).as_posix())
        return (f"{prefix}/resources/quellen/bundle-{idx:02d}.tar.gz", buf.getvalue())

    for f in src:
        if batch and batch_bytes + f.stat().st_size > BUNDLE_TARGET_BYTES:
            bundles.append(flush(len(bundles), batch))
            batch, batch_bytes = [], 0
        batch.append(f)
        batch_bytes += f.stat().st_size
    if batch:
        bundles.append(flush(len(bundles), batch))

    oversized = [(n, b) for n, b in bundles if len(b) > MAX_PART_BYTES]
    if oversized:
        sys.exit(
            f"ERROR: tar.gz-Bündel überschreiten {MAX_PART_BYTES // 1024} KB: "
            + ", ".join(f"{n} ({len(b)//1024} KB)" for n, b in oversized)
        )
    return bundles


def files_from_dir(skill_dir: Path) -> list:
    """Baut die `files`-Liste für den Einzeldatei-Upload eines Skills.

    Alles ausser resources/quellen/ wird einzeln hochgeladen (Pfade NFC-normalisiert).
    Die Quellen werden in tar.gz-Bündel gepackt (siehe _bundle_quellen)."""
    prefix = skill_dir.name
    quellen_dir = skill_dir / "resources" / "quellen"

    files = []
    for f in sorted(skill_dir.rglob("*")):
        if not (f.is_file() and f.suffix.lower() in VALID_EXTENSIONS):
            continue
        if quellen_dir in f.parents:
            continue  # Quellen werden gebündelt
        arc = unicodedata.normalize("NFC", f"{prefix}/{f.relative_to(skill_dir)}")
        files.append((arc, f.read_bytes()))

    if quellen_dir.is_dir():
        files.extend(_bundle_quellen(quellen_dir, prefix))

    # Grenzen prüfen, bevor die API mit kryptischen 400/502 antwortet
    bad = [n for n, _ in files if not SAFE_PATH.match(n)]
    if bad:
        sys.exit(f"ERROR: Pfade mit ungültigen Zeichen: {bad[:5]}")
    big = [(n, len(b)) for n, b in files if len(b) > MAX_PART_BYTES]
    if big:
        sys.exit(f"ERROR: Dateien > {MAX_PART_BYTES // 1024} KB: {big[:5]}")
    if len(files) > MAX_FILES:
        sys.exit(f"ERROR: {len(files)} Dateien > Maximum {MAX_FILES}.")
    total = sum(len(b) for _, b in files)
    if total > MAX_SKILL_BYTES:
        sys.exit(f"ERROR: Skill {total / 1024 / 1024:.1f} MB > {MAX_SKILL_BYTES // 1024 // 1024} MB.")
    print(f"    ({len(files)} Dateien, {total / 1024 / 1024:.2f} MB)")
    return files


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
                    display_title=f"{TENANT}-{name}",
                    files=files_from_dir(skill_dir),
                    betas=BETAS,
                )
                print(f"    Erstellt:     {skill.id}")
                ids[name] = skill.id
        except anthropic.NotFoundError:
            # ID in skill_ids.json existiert nicht mehr bei Anthropic → neu anlegen
            print(f"    Skill-ID ungültig, erstelle neu...")
            skill = client.beta.skills.create(
                display_title=f"{TENANT}-{name}",
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
