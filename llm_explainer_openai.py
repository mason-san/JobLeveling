from dotenv import load_dotenv
from groq import Groq
import os
import re

#LOading the api from the .env file
load_dotenv()
client =  Groq(
    api_key = os.getenv("GROQ_API_KEY"),
)

def get_resume_feedback(resume_text, score, job_description):
    user_prompt = f"""
        Use the exact format below with numbered headings and bullet points (use - for bullets).
        Make sure to use the numbered headings exactly as shown, and do not add any additional text or explanations outside of these sections.
        Given the job description, a candidate resume, and a match score from a resume ranking model,
        perform the following three tasks:\n\n---\n\n
        
        1. My Advice\n\nWrite a helpful, specific summary
        or piece of advice for the candidate based on the match score and how the resume aligns with the job.
        This should feel personalized and encouraging or constructive. Make sure to say the user's name in a professional tone.  \n\n---\n\n

        2. Matching Strengths \n\nList **exactly 3 strengths** where the resume aligns well with the job description.
        Be precise and use short, strong points that could justify the given match score.
        \n\nFormat:\n- [Strength 1]\n- [Strength 2]\n- [Strength 3]\n\n---\n\n

        3. Missing Skills\n\nList **exactly 3 missing or underrepresented skills** in the resume.
        #TO GIVE TO THE LLM 
        job_description = st.session_state.jd
        For each one, briefly explain why it matters for the job description.
        \n\nFormat:\n- [Skill]: [Short explanation]\n- [Skill]: [Short explanation]\n- [Skill]: [Short explanation]\n\n---\n\n

        Job Description:\n{job_description}\n\n

        Resume:\n{resume_text}

        \n\nMatch Score: {score}%\n\n
        """
    
    #CALLING THE API
    response_text = call_groq_model(user_prompt)

    #PARSING THE API AND RETURNING 
    return parse_groq_response(response_text)
    
def parse_groq_response(response_text):
    """
    Robustly parses LLM output with sections:
    1. My Advice
    2. Matching Strengths
    3. Missing Skills
    """
    # Extract sections using regex (non-greedy)
    pattern = re.compile(r"1\.\s*(.*?)\n2\.\s*(.*?)\n3\.\s*(.*)", re.DOTALL)
    match = pattern.search(response_text)
    if not match:
        return {
            "assessment": "Unable to parse assessment.",
            "strengths": [],
            "missing_skills": []
        }
    assessment_raw, strengths_raw, missing_raw = match.groups()

    # Parse strengths (bullets)
    strengths_list = re.findall(r"[-•*]\s*(.+)", strengths_raw)
    if not strengths_list:
        strengths_list = [line.strip() for line in strengths_raw.strip().split("\n") if line.strip()]

    # Parse missing skills (bullets with skill: reason)
    missing_skills = []
    for line in re.findall(r"[-•*]\s*(.+)", missing_raw):
        skill_reason = re.match(r"(.+?):\s*(.+)", line)
        if skill_reason:
            skill, reason = skill_reason.groups()
            missing_skills.append({"skill": skill.strip(), "reason": reason.strip()})
        else:
            missing_skills.append({"skill": line.strip(), "reason": ""})

    return {
        "assessment": assessment_raw.strip(),
        "strengths": strengths_list,
        "missing_skills": missing_skills
    }
            

def call_groq_model(user_prompt):
    try:  
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
            {
                "role": "system",
                "content":"You are an expert AI resume analyst helping job seekers improve their resumes. You evaluate how well a resume matches a given job description and provide clear, helpful, and specific feedback in a professional tone.",
            },
            {
                "role": "user",
                "content": user_prompt,
            }
            ],
            temperature=0.65,
            max_completion_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        output_text = ""
        for chunk in completion:
            content = chunk.choices[0].delta.content or ""
            output_text += content

        print("LLM output: ", output_text) 
        return output_text

    except Exception as e:
        print("An error occured")
        print("Error: ", e)