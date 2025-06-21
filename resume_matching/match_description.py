from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def match_resume_to_job(resume_text: str, job_description: str)->float:
    """
    compares cleaned resume text with job description and returns a similarity score (0.0 to 1.0).
    """

    corpus = [job_description, resume_text]

    vectorizer = TfidfVectorizer()
    tfidf_matrix =  vectorizer.fit_transform(corpus)

    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    return round(similarity_score, 2)