import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

import streamlit as st

import rag.document_loader as document_loader
from rag.text_splitter import split_text
from rag.vector_store import create_vector_store
from rag.retriever import retrieve_chunks

from agents.rag_agent import rag_answer
from search.web_search import web_search

st.set_page_config(page_title="Marketing Strategy AI Copilot")
st.title("🚀 Marketing Strategy AI Copilot")

uploaded_file = st.file_uploader(
    "Upload marketing file (CSV, Excel, or PDF)",
    type=["csv", "xlsx", "pdf"]
)

if uploaded_file:
    st.success("File uploaded successfully")

    # 1. Load + chunk + embed
    raw_text = document_loader.load_documents(uploaded_file)
    chunks = split_text(raw_text)
    vector_store = create_vector_store(chunks)

    # 2. Ask question
    question = st.text_input("Ask a question about your uploaded data")

    if question:
        # 3. Retrieve from uploaded files
        context = retrieve_chunks(vector_store, question)

        # 4. Optional external grounding
        web_context = None
        if len(context.strip()) < 300:
            st.info("Using external web search for additional grounding")
            web_context = web_search(question)

        # 5. Final grounded answer
        answer = rag_answer(context, question, web_context)

        st.subheader("📌 Answer")
        st.write(answer)
