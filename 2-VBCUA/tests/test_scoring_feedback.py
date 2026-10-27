
import pytest

from models.scoring import generate_score
from models.feedback import generate_feedback


@pytest.mark.parametrize(
    ("similarity", "expected_level"),
    [
        (95, "Excellent"),
        (90, "Excellent"),
        (89, "Good"),
        (75, "Good"),
        (74, "Average"),
        (50, "Average"),
        (49, "Needs Improvement"),
        (0, "Needs Improvement"),
    ],
)
def test_scoring_and_feedback_levels_match(similarity, expected_level):
    score = generate_score(similarity)
    feedback = generate_feedback(similarity)

    assert score["level"] == expected_level
    assert feedback["level"] == expected_level


@pytest.mark.parametrize("similarity", [-10, 0, 50, 100, 120])
def test_similarity_is_bounded(similarity):
    score = generate_score(similarity)
    feedback = generate_feedback(similarity)

    assert 0 <= score["overall"] <= 100
    assert score["level"] == feedback["level"]
