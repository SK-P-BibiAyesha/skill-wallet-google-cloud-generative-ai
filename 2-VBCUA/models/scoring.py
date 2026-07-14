def generate_score(similarity):

    if similarity >= 90:
        return {
            "overall": similarity,
            "concept": 95,
            "quality": 92,
            "level": "Excellent"
        }

    elif similarity >= 75:
        return {
            "overall": similarity,
            "concept": 85,
            "quality": 80,
            "level": "Good"
        }

    elif similarity >= 50:
        return {
            "overall": similarity,
            "concept": 65,
            "quality": 60,
            "level": "Average"
        }

    else:
        return {
            "overall": similarity,
            "concept": 40,
            "quality": 35,
            "level": "Needs Improvement"
        }