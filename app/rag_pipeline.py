from langchain_community.vectorstores import FAISS
from utils.embeddings import get_embeddings

from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ask_question(question):

    embeddings = get_embeddings()

    vectorstore = FAISS.load_local(
        "vector_store",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    docs = retriever.get_relevant_documents(question)

    context = ""

    for doc in docs:
        context += doc.page_content + "\n"

    prompt = f"""
You are an AI document assistant.

Answer the question using ONLY the provided context.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return completion.choices[0].message.content