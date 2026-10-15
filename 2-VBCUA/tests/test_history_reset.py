import sqlite3
import sys
import tempfile
import unittest
from contextlib import closing
from pathlib import Path
from unittest.mock import patch

sys.path.append(str(Path(__file__).resolve().parent.parent))

from database.queries import delete_all_reports


class HistoryResetTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.database_path = Path(self.temp_dir.name) / "history.db"
        with closing(sqlite3.connect(self.database_path)) as connection:
            with connection:
                connection.execute(
                    """
                    CREATE TABLE analysis_history (
                        id INTEGER PRIMARY KEY,
                        topic TEXT,
                        overall_score REAL
                    )
                    """
                )
                connection.execute("CREATE TABLE unrelated_data (value TEXT)")
                connection.executemany(
                    """
                    INSERT INTO analysis_history (topic, overall_score)
                    VALUES (?, ?)
                    """,
                    [("Cloud Computing", 80), ("Machine Learning", 90)],
                )
                connection.execute(
                    "INSERT INTO unrelated_data (value) VALUES ('preserve me')"
                )

    def tearDown(self):
        self.temp_dir.cleanup()

    def _delete_history(self):
        def connect_to_test_database():
            return sqlite3.connect(self.database_path)

        with patch(
            "database.queries.get_connection",
            side_effect=connect_to_test_database,
        ):
            return delete_all_reports()

    def test_deletes_only_history_and_returns_deleted_count(self):
        self.assertEqual(self._delete_history(), 2)

        with closing(sqlite3.connect(self.database_path)) as connection:
            self.assertEqual(
                connection.execute(
                    "SELECT COUNT(*) FROM analysis_history"
                ).fetchone()[0],
                0,
            )
            self.assertEqual(
                connection.execute(
                    "SELECT value FROM unrelated_data"
                ).fetchone()[0],
                "preserve me",
            )

    def test_database_error_rolls_back_and_is_propagated(self):
        with closing(sqlite3.connect(self.database_path)) as connection:
            with connection:
                connection.execute(
                    """
                    CREATE TRIGGER prevent_history_delete
                    BEFORE DELETE ON analysis_history
                    BEGIN
                        SELECT RAISE(ABORT, 'deletion blocked');
                    END
                    """
                )

        with self.assertRaisesRegex(sqlite3.IntegrityError, "deletion blocked"):
            self._delete_history()

        with closing(sqlite3.connect(self.database_path)) as connection:
            self.assertEqual(
                connection.execute(
                    "SELECT COUNT(*) FROM analysis_history"
                ).fetchone()[0],
                2,
            )


if __name__ == "__main__":
    unittest.main()
