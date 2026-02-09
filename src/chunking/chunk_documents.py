import os
import re
import pickle
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from dotenv import load_dotenv

load_dotenv()

INPUT_DIR = "data/processed_docs/cleaned"
OUTPUT_FILE = "data/processed_docs/chunks.pkl"

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 800))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 150))


def extract_metadata_from_filename(filename):
    """
    Extract:
    - PDF name
    - PDF page number
    - Report year from filename
    """
    match = re.search(r"(.*\.pdf)_page_(\d+)", filename)

    if match:
        source = match.group(1)
        pdf_page = int(match.group(2))

        # Try extracting year like 2023-24 or 2022-23
        year_match = re.search(r"(20\d{2}[-–]?\d{2})", source)
        if year_match:
            year = year_match.group(1)
        else:
            year = "Unknown Year"

        return source, pdf_page, year

    return filename, "unknown", "unknown"


def load_documents():
    """Load cleaned text files into LangChain Document objects with metadata."""
    documents = []

    for file in os.listdir(INPUT_DIR):
        if file.endswith(".txt"):
            path = os.path.join(INPUT_DIR, file)

            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

            source, page, year = extract_metadata_from_filename(file)

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": source,
                        "page": page,
                        "year": year
                    }
                )
            )


    return documents


def chunk_documents(documents):
    """Split documents into overlapping chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks.")
    return chunks


def main():
    docs = load_documents()
    chunks = chunk_documents(docs)

    with open(OUTPUT_FILE, "wb") as f:
        pickle.dump(chunks, f)

    print("Chunks saved with metadata!")


if __name__ == "__main__":
    main()
