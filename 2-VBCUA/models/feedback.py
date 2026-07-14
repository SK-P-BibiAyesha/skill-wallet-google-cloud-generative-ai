def generate_feedback(similarity):

    if similarity >= 85:
        return {
            "level": "Excellent",
            "color": "success",
            "message": """
✅ Excellent conceptual understanding.

• Covered the important ideas.
• Meaning is very close to the reference.
• Keep it up!
"""
        }

    elif similarity >= 70:
        return {
            "level": "Good",
            "color": "info",
            "message": """
👍 Good explanation.

• Most concepts are correct.
• Add a few more technical details.
"""
        }

    elif similarity >= 50:
        return {
            "level": "Average",
            "color": "warning",
            "message": """
🙂 Average understanding.

• Some concepts are correct.
• Important details are missing.
• Revise the topic once more.
"""
        }

    else:
        return {
            "level": "Needs Improvement",
            "color": "error",
            "message": """
❌ Needs Improvement.

• Review the topic.
• Practice explaining again.
"""
        }