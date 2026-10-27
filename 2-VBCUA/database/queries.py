from database.database import get_connection
from datetime import datetime, timezone
from zoneinfo import ZoneInfo


def insert_analysis(
    topic,
    transcript,
    similarity,
    overall,
    concept,
    quality,
    level,
    feedback,
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO analysis_history(
        topic,
        transcript,
        similarity,
        overall_score,
        concept_accuracy,
        explanation_quality,
        level,
        feedback
    )

    VALUES(?,?,?,?,?,?,?,?)

    """, (
        topic,
        transcript,
        similarity,
        overall,
        concept,
        quality,
        level,
        feedback
    ))

    conn.commit()

    conn.close()


def get_all_reports():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM analysis_history

    ORDER BY created_at DESC

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_all_reports():
    """Delete only analysis-history rows in one transaction and return the row count."""
    conn = get_connection()

    try:
        with conn:
            cursor = conn.execute("DELETE FROM analysis_history")
            return cursor.rowcount
    finally:
        conn.close()