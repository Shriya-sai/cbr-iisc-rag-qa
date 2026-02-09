import os
import pickle
from langchain_community.vectorstores import FAISS
from src.embeddings.embedding_model import get_embedding_model

CHUNKS_FILE = "data/processed_docs/chunks.pkl"
VECTOR_DB_DIR = "data/vector_store"


def load_chunks():
    with open(CHUNKS_FILE, "rb") as f:
        chunks = pickle.load(f)
    return chunks


def build_vector_store():
    print("Loading chunks...")
    chunks = load_chunks()

    print("Loading embedding model...")
    embeddings = get_embedding_model()

    print("Creating FAISS vector store...")
    vector_store = FAISS.from_documents(chunks, embeddings)

    os.makedirs(VECTOR_DB_DIR, exist_ok=True)
    vector_store.save_local(VECTOR_DB_DIR)

    print("Vector store saved locally!")


if __name__ == "__main__":
    build_vector_store()
