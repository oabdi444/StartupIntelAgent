from dotenv import load_dotenv
load_dotenv()
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import agent, summarize_report

import streamlit as st
from app import agent, summarize_report

st.title("Startup Intelligence Agent")
query = st.text_input("Enter a startup space to analyze (e.g., AI legal tech)")

if st.button("Run Analysis"):
    with st.spinner("Researching..."):
        result = agent.run(query)
        summary = summarize_report(result)
        st.subheader("Startup Intelligence Report")
        st.markdown(summary)
