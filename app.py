import streamlit as st
from resume_parser import extract_text_from_pdf
from scoring_engine import score_resume_vs_jd, feedback, load_model
import pandas as pd
from llm_explainer_openai import get_resume_feedback

st.title("Job :blue[Leveling] :sunglasses:")

# Preset job descriptions
jd_templates = {
    "Frontend Developer 👩‍🎨": "We are looking for a Frontend Developer with experience in HTML, CSS, JavaScript, and React.",
    "Backend Developer 🛠️": "We are looking for a Backend Developer skilled in Python, Flask, and RESTful APIs.",
    "Data Analyst 📊": "We are hiring a Data Analyst familiar with SQL, Excel, and Tableau/PowerBI for reporting and analysis."
}

model = load_model()
st.session_state.results = {}

if "jd" not in st.session_state: 
    st.session_state.jd = ""

if "clicked" not in st.session_state:
    st.session_state.clicked = 0

st.markdown("#### Select the type of job")

left, middle, right = st.columns(3)

if left.button("Front End Developer", help="A generic Frontend Developer Job Description", use_container_width=True, type="secondary"):
    st.session_state.jd= jd_templates["Frontend Developer 👩‍🎨"]

if middle.button("Backend Developer", help="A generic Backend Developer Job Description", use_container_width=True):
    st.session_state.jd = jd_templates["Backend Developer 🛠️"]

if right.button("Data Analyst", help="A generic Data Analyst Job Description", use_container_width=True):
    st.session_state.jd = jd_templates["Data Analyst 📊"]


with st.form("File_Uploader"):
    uploaded_file = st.file_uploader( "Upload your resume: ", accept_multiple_files=False, type= "pdf") 
    job_desc_submitted = st.text_area("Job Description", value=st.session_state.jd)

    submitted=st.form_submit_button("Submit")

#VARIABLES TO PASS TO LLM
resume_text = "EMPTY"
job_description = "EMPTY"
score = 0

if submitted:
    if job_desc_submitted and uploaded_file:

        #Clicked for the first time.
        st.session_state.clicked = 1

        st.session_state.results = []

        #Give these to LLM 
        resume_text = extract_text_from_pdf(uploaded_file)
        score = score_resume_vs_jd(resume_text, st.session_state.jd, model)
        label = feedback(score)

        st.session_state.results.append({
            "Name":uploaded_file.name,
            "Resume":resume_text,
            "Score":score,
            "Label" : label, 
            "File" : uploaded_file,
            "Text": resume_text
            })

        #Build dataframe here
        st.session_state.df = pd.DataFrame([{
            "Name": r["Name"].strip('.pdf'), 
            "Score" : r["Score"],
            "Label" : r["Label"],
            "Text" : r["Text"]
        } for r in st.session_state.results])

        st.session_state.parsed_feedback = get_resume_feedback(resume_text, score, job_desc_submitted)

        st.switch_page("pages/reports_new.py")

    else:
        st.warning("Please provide job description and atleast one resume.")

#Sidebar if submit was done before
if st.session_state.clicked > 0:
    st.sidebar.page_link("app.py", label="Home")
    st.sidebar.page_link("pages/reports_new.py", label="Your Report")