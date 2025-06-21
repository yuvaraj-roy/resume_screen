import streamlit as st
from resume_input.resume_converter import convert_to_text
from resume_matching.match_description import match_resume_to_job
from score.resume_score import calculate_resume_score
from analysis.matching_skills import get_matching_skills
from analysis.unmatching_skills import get_unmatched_skills

st.title("🧠 Resume Screening Tool")

uploaded_file = st.file_uploader("Upload Resume (.pdf or .docx)", type=["pdf", "docx"])

job_description = st.text_area("Paste Job Description Here")

job_skills = st.text_input("Enter required skills (comma-separated)", value="Python, SQL, Machine Learning, Pandas, Communication")

if st.button("Analyze Resume") and uploaded_file and job_description:
    resume_filename = f"temp_resume.{uploaded_file.name.split('.')[-1]}"
    with open(resume_filename, "wb") as f:
        f.write(uploaded_file.read())

    resume_text = convert_to_text(resume_filename)

    if not resume_text.strip():
        st.error("Failed to read the resume file.")
    else:
        similarity = match_resume_to_job(resume_text, job_description)
        score = calculate_resume_score(similarity)
        skills_list = [skill.strip() for skill in job_skills.split(",")]

        matched = get_matching_skills(resume_text, skills_list)
        unmatched = get_unmatched_skills(resume_text, skills_list)

        st.subheader("📊 Results")
        st.write(f"**Similarity Score**: {similarity:.2f}")
        st.write(f"**Resume Score**: {score}/100")
        st.write(f"✅ Matching Skills: {matched}")
        st.write(f"❌ Missing Skills: {unmatched}")
