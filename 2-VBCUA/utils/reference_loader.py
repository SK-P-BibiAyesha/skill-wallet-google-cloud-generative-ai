
from pathlib import Path

REFERENCE_FILES = {
    "Machine Learning": "machine_learning.txt",
    "Artificial Intelligence": "artificial_intelligence.txt",
    "Cloud Computing": "cloud_computing.txt",
    "Data Science": "data_science.txt",
    "Database Management System": "dbms.txt",
    "Operating System": "operating_system.txt",
}


def load_reference(topic):
    filename = REFERENCE_FILES.get(topic)

    if filename is None:
        raise ValueError(f"Unknown topic: {topic}")

    project_root = Path(__file__).resolve().parent.parent
    filepath = project_root / "reference_concepts" / filename

    if not filepath.is_file():
        raise FileNotFoundError(
            f"Reference file not found for {topic}: {filepath}"
        )

    content = filepath.read_text(encoding="utf-8").strip()

    if not content:
        raise ValueError(f"Reference file is empty: {filepath}")

    return content
