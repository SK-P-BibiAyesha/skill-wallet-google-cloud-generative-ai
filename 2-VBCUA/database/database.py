import sqlite3
from pathlib import Path

DATABASE_NAME = (
    Path(__file__).parent / "database.db"
)


def get_connection():
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