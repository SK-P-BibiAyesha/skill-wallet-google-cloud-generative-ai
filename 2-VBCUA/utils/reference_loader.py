import os

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
        return ""

    filepath = os.path.join("reference_concepts", filename)

    if not os.path.exists(filepath):
        return ""

    with open(filepath, "r", encoding="utf-8") as file:
        return file.read().strip()