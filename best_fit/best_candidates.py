from resume_matching.match_description import match_resume_to_job
from score.resume_score import calculate_resume_score

def rank_candidates(resume_texts: list, job_description: str) -> list:
    """
    Takes a list of resume texts and a job description.
    Returns a list of tuples (index, score), sorted by best match.
    """

    results=[]

    for idx, resume in enumerate(resume_texts):
        similarity = match_resume_to_job(resume, job_description)
        score = calculate_resume_score(similarity)
        results.append((idx, score))

    results.sort(key=lambda x: x[1], reverse=True)
    return results