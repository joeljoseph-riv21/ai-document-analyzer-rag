from utils.document_loader import load_documents
from utils.text_splitter import split_documents
from utils.embeddings import get_embeddings

from langchain_community.vectorstores import FAISS


def create_vector_store(file_path):

    print("Loading document...")

    documents = load_documents(file_path)

    print("Splitting document...")

    chunks = split_documents(documents)

    print("Generating embeddings...")

    embeddings = get_embeddings()

    print("Creating FAISS vector store...")

    vectorstore = FAISS.from_documents(chunks, embeddings)

    vectorstore.save_local("vector_store")

    print("Vector database created successfully!")