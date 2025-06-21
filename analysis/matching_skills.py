def get_matching_skills(resume_text: str,job_skills: list) -> list:
    """
    Return a list of job skills that are found in the resume text.
    """

    resume_text_lower=resume_text.lower()
    matched = [skill for skill in job_skills if skill.lower() in resume_text_lower]
    return matched