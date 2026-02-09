## 📂 Project Structure
cbr-iisc-rag-qa/
│
├── app/                  # Streamlit UI
├── src/
│   ├── ingestion/        # PDF download + parsing
│   ├── chunking/         # Text chunking
│   ├── embeddings/       # Embedding + FAISS DB
│   ├── rag/              # RAG pipeline
│   ├── evaluation/       # Evaluation scripts
│   └── utils/            # Config + report links
│
├── tests/                # Basic tests
├── requirements.txt
└── README.md
