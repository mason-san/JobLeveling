import streamlit as st

st.set_page_config(layout="wide")

st.markdown("# 📊 Your Report")

# Sidebar links
st.sidebar.page_link("app.py", label="Home")
st.sidebar.page_link("pages/reports_new.py", label="Your Report")

# Check if the report data is in the session
if 'df' not in st.session_state or 'parsed_feedback' not in st.session_state:
    st.error("Please upload a resume and provide a job description on the Home page to generate a report.")
    st.page_link("app.py", label="Go to Home", icon="🏠")
    st.stop()

# Extract data from session state
strengths = st.session_state.parsed_feedback.get('strengths', [])
assessment = st.session_state.parsed_feedback.get('assessment', "No assessment was generated.")
missing_skills = st.session_state.parsed_feedback.get('missing_skills', [])
df = st.session_state.df

# --- Report Display ---
for index, row in df.iterrows():
    name = row['Name']
    score = row['Score']

    with st.container(border=True):
        # --- Header ---
        col1, col2 = st.columns([4, 1])
        with col1:
            st.subheader(f"Analysis for {name}")
            st.markdown(f"{assessment}")
        with col2:
            st.metric(label="Match Score", value=f"{score:.0f}%", help="This score represents the semantic match between your resume and the job description.")

        st.divider()

        # --- Details ---
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### ✅ Matching Strengths")
            if strengths:
                for strength in strengths:
                    st.markdown(f"- {strength}")
            else:
                st.info("No specific matching strengths were identified.")
        
        with col2:
            st.markdown("#### 🔍 Missing Skills")
            if missing_skills:
                for skill in missing_skills:
                    with st.expander(f"**{skill['skill']}**", expanded=True):
                        st.write(skill['reason'])
            else:
                st.info("No specific missing skills were identified.")