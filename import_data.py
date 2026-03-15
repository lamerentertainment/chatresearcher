"""
Import Präjudizen CSV into SQLite database.
Usage: python import_data.py <path-to-csv>
"""
import csv
import sys
from dotenv import load_dotenv

load_dotenv()

from app.database import init_db, db


def import_csv(filepath: str):
    init_db()

    with open(filepath, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("CSV is empty.")
        return

    print(f"Importing {len(rows)} rows...")

    with db() as conn:
        # Clear existing data and rebuild FTS
        conn.execute("DELETE FROM praejudizen")
        conn.execute("DELETE FROM praejudizen_fts")

        for row in rows:
            conn.execute(
                "INSERT INTO praejudizen (titel, regeste, urteilsauszug) VALUES (?, ?, ?)",
                (
                    row.get("Titel", "").strip(),
                    row.get("Regeste", "").strip(),
                    row.get("Urteilsauszug", "").strip(),
                ),
            )

    # Verify
    with db() as conn:
        count = conn.execute("SELECT COUNT(*) FROM praejudizen").fetchone()[0]
    print(f"Done. {count} Präjudizen imported.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python import_data.py <path-to-csv>")
        sys.exit(1)
    import_csv(sys.argv[1])
