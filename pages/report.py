import streamlit as st
from llm_explainer_openai import call_groq_model

st.markdown("# REPORT")

#sidebar
st.sidebar.page_link("app.py", label="Home")
st.sidebar.page_link("pages/report.py", label="Your Report")

#IF no session
if 'df' not in st.session_state:
    st.error("Please complete the form first to generate a report.")
    st.stop()

strengths = st.session_state.parsed_feedback['strengths']
assesment = st.session_state.parsed_feedback['assessment']
missing_skills = st.session_state.parsed_feedback['missing_skills']

#MAKE A RESPONSIVE CARD DESIGN
for index, row in st.session_state.df.iterrows():
    st.subheader(f"Name: {row['Name']}")
    st.write(f"Score: {row['Score']:.0f}%")

    if assesment:
        st.write("### Assessment")
        st.markdown(assesment)
    
    # Display strengths
    if strengths:
        st.write("### Matching Strengths:")
        for strength in strengths:
            st.markdown(f"- {strength}")

    # Display missing skills
    if missing_skills:
        st.write("### Missing Skills:")
        for skill in missing_skills:
            st.markdown(f"- **{skill['skill']}**: {skill['reason']}")
    
    st.markdown("---")  # Separator between resumes