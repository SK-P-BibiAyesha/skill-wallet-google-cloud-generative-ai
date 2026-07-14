import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from models.semantic_model import calculate_similarity


def test_semantic_model():
    """
    Test Sentence-BERT semantic similarity.
    """

    reference_text = (
        "Cloud computing provides on demand access "
        "to computing resources over the internet."
    )

    student_text = (
        "Cloud computing allows users to access "
        "computing resources through the internet."
    )

    score = calculate_similarity(
        reference_text,
        student_text
    )

    print(f"Similarity Score: {score}")

    # Check data type
    assert isinstance(score, float)

    # Score should be between 0 and 100
    assert 0 <= score <= 100

    # Similar texts should have a reasonably high score
    assert score >= 60

    print("✅ Semantic Model Test Passed")


if __name__ == "__main__":
    test_semantic_model()