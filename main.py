import os.path
from http.cookiejar import unmatched

from resume_input.resume_converter import convert_to_text
from resume_matching.match_description import match_resume_to_job
from score.resume_score import calculate_resume_score
from analysis.matching_skills import get_matching_skills
from analysis.unmatching_skills import get_unmatched_skills

print("✅ Script started...")
def main():
    resume_path = "sample_resume.pdf"
    if not os.path.exists(resume_path):
        print("Not found")
        return
    else:
        print("file found")
    job_description="""
    We are looking for a Python Developer with experience in machine learning, SQL, and data analysis.
    Required skills: Python, SQL, Machine Learning, Pandas, Communication
    """
    job_skills=["Python", "SQL", "Machine Learning", "Pandas", "Communication"]
    print("Converting resume to text...")
    resume_text = convert_to_text(resume_path)
    if not resume_text.strip():
        print("Text empty")
        return
    else:
        print("Text loaded")
    print("Resume Text (first 200 chars):", resume_text[:200])
    print("Matching resume to job description...")

    similarity = match_resume_to_job(resume_text, job_description)
    print("Similarity score:", similarity)


    score = calculate_resume_score(similarity)
    matched = get_matching_skills(resume_text, job_skills)
    unmatched = get_unmatched_skills(resume_text,job_skills)

    print("\n Resume Analysis Report")
    print(f" Similarity score: {similarity}")
    print(f"Resume score: {score/100}")
    print(f"Matching skills: {matched}")
    print(f"Missing skills: {unmatched}")


if __name__=='__main__':
    main()
