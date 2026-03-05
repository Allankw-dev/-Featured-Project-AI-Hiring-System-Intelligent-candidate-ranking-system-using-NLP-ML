import streamlit as st
import requests
from datetime import datetime

# Page setup
st.set_page_config(page_title="AI Hiring System", layout="centered")
st.title("🤖 AI Hiring Intelligence System")
st.markdown("Automated resume screening system using AI and NLP.")

# Candidate Analysis Section
st.header("Candidate Analysis")

name = st.text_input("Candidate Name")
resume_text = st.text_area("Paste Resume Text")
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze Candidate"):
    if not name or not resume_text or not job_desc:
        st.warning("Please fill all fields!")
    else:
        with st.spinner("Analyzing candidate..."):
            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                json={
                    "name": name,
                    "resume_text": resume_text,
                    "job_description": job_desc
                }
            )

        if response.status_code == 200:
            data = response.json()
            st.success(f"✅ Match Score: **{round(data['match_score'],2)}%**")
            st.info(f"🧑‍💼 Estimated Experience: **{data['experience']} years**")
        else:
            st.error("Something went wrong while analyzing.")

st.markdown("---")

# View All Candidates Section
st.header("All Candidates")
if st.button("Refresh Candidate List"):
    response = requests.get("http://127.0.0.1:8000/candidates")
    if response.status_code == 200:
        candidates = response.json()
        if candidates:
            # Convert list of dicts to a table
            st.table(candidates)
        else:
            st.info("No candidates found yet.")
    else:
        st.error("Failed to fetch candidates.")