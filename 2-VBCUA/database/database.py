import os
import sqlite3
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env", override=False)

DATABASE_NAME = Path(
    os.environ.get("VBCUA_DATABASE_PATH")
    or Path(__file__).parent / "database.db"
).expanduser()


def get_connection():
    DATABASE_NAME.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DATABASE_NAME)


def create_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analysis_history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        topic TEXT,

        transcript TEXT,

        similarity REAL,

        overall_score REAL,

        concept_accuracy REAL,

        explanation_quality REAL,

        level TEXT,

        feedback TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    conn.commit()

    conn.close()