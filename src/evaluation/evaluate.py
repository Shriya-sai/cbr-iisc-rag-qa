from src.rag.retriever import get_retriever
from src.rag.rag_pipeline import ask_question
from src.evaluation.test_questions import TEST_QUESTIONS


def evaluate_retrieval():
    retriever = get_retriever()

    print("\n==============================")
    print(" RETRIEVAL EVALUATION")
    print("==============================\n")

    for question in TEST_QUESTIONS:
        docs = retriever.get_relevant_documents(question)

        print(f"\nQuestion: {question}")
        print("Top retrieved sources:")

        for doc in docs:
            source = doc.metadata.get("source")
            page = doc.metadata.get("page")
            print(f"  - {source}, Page {page}")

        print("-" * 40)


def evaluate_generation():
    print("\n==============================")
    print(" GENERATION EVALUATION")
    print("==============================\n")

    for question in TEST_QUESTIONS:
        print(f"\nQuestion: {question}\n")

        answer = ask_question(question)

        print("Answer:")
        print(answer)
        print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    evaluate_retrieval()
    evaluate_generation()
