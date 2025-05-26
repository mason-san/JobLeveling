def generate_explanation_prompt(job_desc, resume_text):
    return f"""
        Compare this resume to the job description below.

        Give a short, clean summary like this:

        Match: [3 key matching skills]
        Missing: [2 missing critical skills]
        Summary: [One sentence. Max 20 words.]
        Assessment: Strong / Moderate / Weak

        Job Description:
        {job_desc}

        Resume:
        {resume_text}
    """



import requests

def get_explanation_from_ollama(prompt, model="deepseek-r1:1.5b"):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict":150,
                    "temperature":0.3
                }
            }
        )

        # Check status and dump full response
        print("Status code:", response.status_code)
        print("Raw response:", response.text)

        data = response.json()
        raw = data.get("response", "⚠️ No valid response.")
        return raw[:700] + "..." if len(raw) > 700 else raw
    except Exception as e:
        return f"❌ Error talking to Ollama: {e}"