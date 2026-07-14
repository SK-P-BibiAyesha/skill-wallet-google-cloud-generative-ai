import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from database.database import (
    create_table,
    get_connection
)


def test_database():
    """
    Test database creation and connection.
    """

    # Create the table
    create_table()

    # Connect to database
    conn = get_connection()

    cursor = conn.cursor()

    # Verify table exists
    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name='analysis_history'
    """)

    table = cursor.fetchone()

    assert table is not None
    assert table[0] == "analysis_history"

    conn.close()

    print("✅ Database Test Passed")


if __name__ == "__main__":
    test_database() 