from app.rag_pipeline import ask_question

while True:

    question = input("\nAsk a question about the document: ")

    if question.lower() == "exit":
        break

    answer = ask_question(question)

    print("\nAI Answer:\n")
    print(answer)