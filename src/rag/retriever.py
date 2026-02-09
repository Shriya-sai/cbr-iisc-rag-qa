from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

VECTOR_DB_PATH = "data/vector_store"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def get_retriever():
    # Load embedding model
    embeddings = HuggingFaceEmbeddings(model_name=MODEL_NAME)

    # Load FAISS vector store from disk
    vectorstore = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Use MMR retrieval to reduce duplicate chunks
    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 4, "fetch_k": 10}
    )

    return retriever
