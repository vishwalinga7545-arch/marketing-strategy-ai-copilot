import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from utils.file_loader import load_marketing_file, summarize_dataframe
from agents.data_analyst_agent import analyze_marketing_data

st.title("Marketing Strategy AI Copilot")

uploaded_file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])

if uploaded_file:
    df = load_marketing_file(uploaded_file)
    st.dataframe(df.head())

    if st.button("Analyze with AI"):
        summary = summarize_dataframe(df)
        insights = analyze_marketing_data(summary)
        st.write(insights)
