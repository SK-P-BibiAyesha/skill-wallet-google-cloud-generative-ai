import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from models.keyword_match import match_keywords


def test_keyword_match():
    """
    Test keyword matching functionality.
    """

    reference_text = (
        "Cloud computing provides on demand access to servers, "
        "storage, databases, networking and software over the internet."
    )

    student_text = (
        "Cloud computing allows users to access servers, storage "
        "and software through the internet."
    )

    result = match_keywords(reference_text, student_text)

    print("Keyword Matching Result:")
    print(result)

    # Check return type
    assert isinstance(result, dict)

    # Check required keys
    assert "matched" in result
    assert "missing" in result
    assert "score" in result
    assert "matched_count" in result
    assert "total" in result

    # Check data types
    assert isinstance(result["matched"], list)
    assert isinstance(result["missing"], list)
    assert isinstance(result["score"], float)
    assert isinstance(result["matched_count"], int)
    assert isinstance(result["total"], int)

    # Score should be between 0 and 100
    assert 0 <= result["score"] <= 100

    # At least one keyword should match
    assert result["matched_count"] > 0

    # Total keywords should be greater than zero
    assert result["total"] > 0

    print("✅ Keyword Match Test Passed")


if __name__ == "__main__":
    test_keyword_match()