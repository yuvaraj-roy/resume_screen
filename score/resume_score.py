def calculate_resume_score(similarity: float)->int:
    """
    Converts a similarity score (0.0 to 0.1) into a 0-100 resume score.
    """

    score = round(similarity*100)
    return score