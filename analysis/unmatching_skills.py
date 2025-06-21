from http.cookiejar import unmatched


def get_unmatched_skills(resume_text: str, job_skills: list)->list:
    """
    Return a list of job-required skills that are NOT found in the resume.
    """

    resume_text_lower = resume_text.lower()
    unmatched = [skill for skill in job_skills if skill.lower() not in resume_text_lower]
    return unmatched