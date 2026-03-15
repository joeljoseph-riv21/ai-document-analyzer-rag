import streamlit as st
import os

from app.rag_pipeline import ask_question
from app.ingest import create_vector_store

st.title("📄 AI Document Analyzer")

st.write("Upload a document and ask questions about it.")

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# File uploader
uploaded_file = st.file_uploader(
    "Upload a document",
    type=["pdf", "txt"]
)

if uploaded_file:

    file_path = os.path.join("data", uploaded_file.name)

    # Save uploaded file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Document uploaded successfully!")

    # Process button
    if st.button("Process Document"):

        with st.spinner("Processing document..."):
            create_vector_store(file_path)

        st.success("Document processed and vector database created!")

st.divider()

st.write("### Ask questions about the document")

question = st.text_input("Enter your question")

if st.button("Ask"):

    if question:

        with st.spinner("Generating answer..."):
            answer = ask_question(question)

        st.subheader("Answer")
        st.write(answer)

    else:
        st.warning("Please enter a question.")