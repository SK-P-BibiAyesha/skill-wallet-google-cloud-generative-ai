
def generate_feedback(similarity):
    """Generate feedback using the same thresholds as scoring.py."""

    similarity = max(0.0, min(100.0, float(similarity)))

    if similarity >= 90:
        return {
            "level": "Excellent",
            "color": "success",
            "message": (
                "Excellent conceptual understanding.\n\n"
                "- Your explanation closely matches the reference.\n"
                "- Review any remaining gaps in technical detail.\n"
                "- Continue practicing with examples."
            ),
        }

    elif similarity >= 75:
        return {
            "level": "Good",
            "color": "info",
            "message": (
                "Good explanation.\n\n"
                "- Most important concepts are covered.\n"
                "- Add missing technical details and examples.\n"
                "- Review the reference topic."
            ),
        }

    elif similarity >= 50:
        return {
            "level": "Average",
            "color": "warning",
            "message": (
                "Developing conceptual understanding.\n\n"
                "- Some concepts align with the reference.\n"
                "- Review important missing details.\n"
                "- Practice explaining the topic again."
            ),
        }

    else:
        return {
            "level": "Needs Improvement",
            "color": "error",
            "message": (
                "More practice is recommended.\n\n"
                "- Review the reference topic carefully.\n"
                "- Identify the main ideas.\n"
                "- Try explaining the topic again."
            ),
        }
