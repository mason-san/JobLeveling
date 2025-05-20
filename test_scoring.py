from scoring_engine import score_resume_vs_jd, feedback

fake_jd = """
We are looking for a software engineer with experience in Python, Flask, and REST APIs.
Must be comfortable with cloud platforms and have good communication skills.
"""

fake_resume = """
Good communication skills. Good Cloud platform skills 
"""

if __name__ == "__main__":
    resume_score = score_resume_vs_jd(fake_jd, fake_resume)
    print("\n===== SCORE & FEEDBACK =====")
    print("The score",resume_score,"feedback is" , feedback(resume_score))