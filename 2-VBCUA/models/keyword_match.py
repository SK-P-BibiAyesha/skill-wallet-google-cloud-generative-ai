import re


def extract_keywords(text):
    """
    Extract important keywords from text.
    """

    stop_words = {
        "the", "is", "a", "an", "of", "to", "and",
        "that", "from", "with", "for", "on",
        "in", "it", "as", "by", "be", "are",
        "this", "these", "those", "their",
        "its", "or", "at", "into", "than",
        "over", "under", "using", "used",
        "can", "will", "which", "without"
    }

    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

    keywords = []

    for word in words:
        if len(word) > 3 and word not in stop_words:
            keywords.append(word)

    return sorted(set(keywords))


def match_keywords(reference_text, student_text):
    """
    Compare keywords from reference and student explanation.
    """

    reference_keywords = extract_keywords(reference_text)
    student_keywords = extract_keywords(student_text)

    matched = []
    missing = []

    for keyword in reference_keywords:
        if keyword in student_keywords:
            matched.append(keyword)
        else:
            missing.append(keyword)

    score = 0

    if len(reference_keywords) > 0:
        score = round(
            len(matched) / len(reference_keywords) * 100,
            2
        )

    return {
        "matched": matched,
        "missing": missing,
        "score": score,
        "matched_count": len(matched),
        "total": len(reference_keywords),
    }