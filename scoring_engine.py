from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

def score_resume_vs_jd(resume_text, job_desc, model):
    resume_vec = model.encode([resume_text])
    job_vec = model.encode([job_desc])
    score = cosine_similarity(resume_vec, job_vec)[0][0]
    return round(score * 100, 2)

def feedback(score):
    if score > 80: 
        return "Strong Match!"
    elif score > 60: 
        return "Decent Match"
    else: 
        return "Low Match not proper"
    

