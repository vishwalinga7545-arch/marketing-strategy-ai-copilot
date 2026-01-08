import streamlit as st
import pandas as pd

st.set_page_config(page_title="Marketing Strategy AI Copilot")

st.title("🚀 Marketing Strategy AI Copilot")
st.write("Upload your marketing data (Excel or CSV)")

uploaded_file = st.file_uploader(
    "Upload marketing data file",
    type=["xlsx", "csv"]
)
##DISPLAY DATA

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📊 Uploaded Data Preview")
    st.dataframe(df.head())
