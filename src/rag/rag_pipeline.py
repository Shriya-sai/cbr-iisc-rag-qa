from src.utils.report_links import REPORT_LINKS
from langchain_community.llms import Ollama
from src.rag.retriever import get_retriever
from src.rag.prompt_template import RAG_PROMPT_TEMPLATE


def format_docs(docs):
    context = ""

    for doc in docs:
        source = doc.metadata.get("source", "unknown")
        page = doc.metadata.get("page", "unknown")
        year = doc.metadata.get("year", "unknown")

        context += f"\n[Source: CBR Annual Report {year}, PDF Page: {page}]\n"
        context += doc.page_content
        context += "\n\n"

    return context



def build_rag_chain():
    """Create retriever + LLM."""
    retriever = get_retriever()
    llm = Ollama(model="mistral")
    return retriever, llm


def ask_question(question: str):
    retriever, llm = build_rag_chain()

    docs = retriever.get_relevant_documents(question)
    context = format_docs(docs)

    prompt = RAG_PROMPT_TEMPLATE.format(
        context=context,
        question=question
    )

    answer = llm.invoke(prompt)

    # Collect unique sources
    sources = set()
    for doc in docs:
        year = doc.metadata.get("year", "unknown")
        page = doc.metadata.get("page", "unknown")
        link = REPORT_LINKS.get(year, "")
        sources.add((year, page, link))


    return answer, sorted(list(sources))



if __name__ == "__main__":
    while True:
        q = input("\nAsk a question (or type 'exit'): ")
        if q.lower() == "exit":
            break

        response = ask_question(q)
        print("\nAnswer:\n")
        print(response)
