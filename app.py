import streamlit as st
from resume_parser import extract_text_from_pdf
from scoring_engine import score_resume_vs_jd, feedback, load_model
from sentence_transformers import SentenceTransformer
from llm_explainer import generate_explanation_prompt, get_explanation_from_ollama
import pandas as pd

st.title("Job :blue[Leveling] :sunglasses:")

with st.form("Job_detail_form"):
    job_desc = st.text_area("Paste the Job Description below:", height=400)
    uploaded_files = st.file_uploader(
        "Upload One or more Candidate Resumes (PDF only)", accept_multiple_files=True, type= "pdf"
    )
    submitted=st.form_submit_button("Submit")

model = load_model()
st.session_state.results = {}

if submitted:
    if job_desc and uploaded_files:

        st.session_state.jd_text = job_desc
        st.session_state.results = []

        for uploaded_file in uploaded_files:
            uploaded_file.seek(0)
            resume_text = extract_text_from_pdf(uploaded_file)
            score = score_resume_vs_jd(resume_text, job_desc, model)
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

    else:
        st.warning("Please provide job description and atleast one resume.")


#Interactive Table to be displayed
#Sort by score

if "df" in st.session_state and not st.session_state.df.empty:
    sorted_results = sorted(st.session_state.results, key = lambda x: x["Score"], reverse=True)

    for result in sorted_results:
        with st.expander(f"{result['Name']} — {result['Score']:.0f}%"):
            col1, col2 = st.columns([3, 1])
            col1.markdown(f"**Match Level:** {result['Label']}")
            col2.markdown(f"**Score:** {result['Score']:.0f}%") 

            result['File'].seek(0)

    data_encoded = st.session_state.df.to_csv(index=False).encode('utf-8')

    if st.button("Export results as CSV"):
        st.download_button("Download CSV", data=data_encoded, file_name="resume_scores.csv", mime="text/csv")

    #Bar Chart
    st.write("### Score Visualization.")
    st.bar_chart(st.session_state.df.set_index('Name')['Score'])

#Now the Ollama deepseek use
#Sort the results by score 
top_results = sorted(st.session_state.results, key=lambda x: x["Score"], reverse=True)[:5]

#For each, generate explanation
for res in top_results:
    resume_text = res["Text"]
    prompt = generate_explanation_prompt(st.session_state.jd_text, resume_text)
    explanation = get_explanation_from_ollama(prompt)
    res["explanation"] = explanation

    if "explanation" in res and "⚠️" not in res["explanation"]:
        st.markdown("**Explanation:**")
        st.markdown(result["explanation"])
    else:
        st.warning("Explanation could not be generated.")