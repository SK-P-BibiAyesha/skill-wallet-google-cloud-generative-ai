
def generate_score(similarity):
    """Generate assessment scores from semantic similarity."""

    similarity = max(0.0, min(100.0, float(similarity)))

    if similarity >= 90:
        level = "Excellent"
        concept = 95
        quality = 92
    elif similarity >= 75:
        level = "Good"
        concept = 85
        quality = 80
    elif similarity >= 50:
        level = "Average"
        concept = 65
        quality = 60
    else:
        level = "Needs Improvement"
        concept = 40
        quality = 35

    return {
        "overall": round(similarity, 2),
        "concept": concept,
        "quality": quality,
        "level": level,
    }
