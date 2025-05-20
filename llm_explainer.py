def generate_explanation_prompt(job_desc, resume_text):
    return f"""
You are an AI resume expert.

Compare the following candidate resume to the job description. Briefly explain:
- What skills and experience match
- What skills are missing
- A 1-line summary of suitability
- A final label: Strong / Moderate / Weak match

Job Description:
{job_desc}

Resume:
{resume_text}

Return in this format:
Match: [...]
Missing: [...]
Summary: [...]
Final Assessment: [...]
"""

import requests

def get_explanation_from_ollama(prompt, model="deepseek"):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model":model,
            "prompt":prompt,
            "stream":False
        }
    )
    return response.json()["response"]

