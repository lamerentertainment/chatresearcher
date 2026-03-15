import sqlite3
import os
from contextlib import contextmanager

DB_PATH = os.getenv("DB_PATH", "data/praejudizen.db")


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@contextmanager
def db():
    conn = get_connection()
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with db() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS praejudizen (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                titel         TEXT NOT NULL,
                regeste       TEXT,
                urteilsauszug TEXT
            );

            CREATE VIRTUAL TABLE IF NOT EXISTS praejudizen_fts USING fts5(
                titel,
                regeste,
                urteilsauszug,
                content='praejudizen',
                content_rowid='id'
            );

            CREATE TRIGGER IF NOT EXISTS praejudizen_ai
            AFTER INSERT ON praejudizen BEGIN
                INSERT INTO praejudizen_fts(rowid, titel, regeste, urteilsauszug)
                VALUES (new.id, new.titel, new.regeste, new.urteilsauszug);
            END;

            CREATE TRIGGER IF NOT EXISTS praejudizen_ad
            AFTER DELETE ON praejudizen BEGIN
                INSERT INTO praejudizen_fts(praejudizen_fts, rowid, titel, regeste, urteilsauszug)
                VALUES ('delete', old.id, old.titel, old.regeste, old.urteilsauszug);
            END;
        """)
