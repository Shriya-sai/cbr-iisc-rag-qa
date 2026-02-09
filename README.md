# 🧠 CBR IISc Annual Report QA — Local RAG System

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![RAG](https://img.shields.io/badge/LLM-RAG-green)
![Ollama](https://img.shields.io/badge/LLM-Mistral-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A fully local **Retrieval Augmented Generation (RAG)** question-answering system that answers questions about the last 3 years of annual reports from the **Centre for Brain Research (CBR), IISc**.

This project was built as an end-to-end Machine Learning + LLM engineering project for technical interviews.

---

## ✨ Features

- 🏠 100% **local** — no paid APIs
- 🔓 Uses **open-source LLM (Mistral via Ollama)**
- 📄 Answers questions from real PDF reports
- 📌 Provides **citations with year + page**
- ✅ Includes **evaluation pipeline**
- 💬 Comes with a **Streamlit chat UI**

---

## 🎥 Demo

Ask questions like:
- *What is the GenomeIndia project?*
- *What studies does CBR conduct on aging?*
- *Who funds the GenomeIndia project?*

The system retrieves relevant report sections and generates grounded answers with citations.

---

## 🏗️ System Architecture
```mermaid
flowchart LR
    A[User Question] --> B[Retriever<br/>FAISS Vector DB]
    B --> C[Relevant Document Chunks]
    C --> D[Prompt Builder]
    D --> E[Local LLM<br/>Mistral via Ollama]
    E --> F[Answer + Citations]
```

### Pipeline Overview

1. **Data Ingestion**
   - Automatically downloads latest CBR annual reports (PDFs)
   - Extracts text page-by-page

2. **Pre-processing**
   - Cleans and normalizes text
   - Splits into semantic chunks

3. **Embedding + Vector Store**
   - SentenceTransformer embeddings
   - FAISS local vector database

4. **RAG Pipeline**
   - Retrieve relevant chunks
   - Build grounded prompt
   - Generate answer with citations

5. **Evaluation**
   - Retrieval quality testing
   - Answer faithfulness testing

6. **User Interface**
   - Streamlit chat app

---

## 📂 Project Structure
```mermaid
graph TD
    A[cbr-iisc-rag-qa/] --> B[app/]
    A --> C[src/]
    A --> D[tests/]
    A --> E[requirements.txt]
    A --> F[README.md]
    
    B --> B1[streamlit_app.py]
    
    C --> C1[ingestion/]
    C --> C2[chunking/]
    C --> C3[embeddings/]
    C --> C4[rag/]
    C --> C5[evaluation/]
    C --> C6[utils/]
    
    C1 --> C1A[download_reports.py]
    C1 --> C1B[pdf_parser.py]
    C1 --> C1C[text_cleaning.py]
    
    C2 --> C2A[chunk_documents.py]
    
    C3 --> C3A[build_vector_store.py]
    
    C4 --> C4A[rag_pipeline.py]
    
    C5 --> C5A[evaluate.py]
    
    C6 --> C6A[config.py]
    C6 --> C6B[report_links.py]
```

---

## 🛠️ Tech Stack

| Component | Tool |
|-----------|------|
| Language | Python |
| LLM | Mistral (Ollama) |
| Framework | LangChain |
| Embeddings | SentenceTransformers |
| Vector DB | FAISS (local) |
| UI | Streamlit |
| PDF Parsing | pdfplumber |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/cbr-iisc-rag-qa.git
cd cbr-iisc-rag-qa
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Install Ollama

Download from: https://ollama.com
```bash
ollama pull mistral
ollama serve
```

---

## 📥 Build the Knowledge Base
```bash
python -m src.ingestion.download_reports
python -m src.ingestion.pdf_parser
python -m src.ingestion.text_cleaning
python -m src.chunking.chunk_documents
python -m src.embeddings.build_vector_store
```

---

## 💬 Run the Assistant (Terminal)
```bash
python -m src.rag.rag_pipeline
```

---

## 🖥️ Run the Web App
```bash
streamlit run app/streamlit_app.py
```

Open in browser: http://localhost:8501

---

## 📊 Evaluation

Run the evaluation suite:
```bash
python -m src.evaluation.evaluate
```

This tests:
- ✅ Retrieval relevance
- ✅ Generation faithfulness
- ✅ Citation grounding

---

## 🎯 Design Decisions

### Why RAG?
- Annual reports are long, domain-specific documents
- RAG grounds LLM responses in real documents and prevents hallucinations

### Why Local LLM?
- ✅ No paid APIs
- ✅ Fully offline
- ✅ Reproducible
- ✅ Demonstrates real engineering skills

### Why FAISS?
- ⚡ Fast local similarity search
- 🏠 No external infrastructure required

### Why PDF Page Citations?
- Annual reports have inconsistent printed page numbers
- Using deterministic PDF page numbers ensures reliable and verifiable citations

---

## 🧪 Evaluation Strategy

We evaluate two aspects:

### Retrieval Quality
Check whether top-k retrieved pages are relevant for benchmark questions.

### Answer Faithfulness
Verify that generated answers:
- ✅ Use retrieved context
- ✅ Provide citations
- ✅ Avoid hallucinations

---

## 🚀 Future Improvements

- [ ] Hybrid search (BM25 + embeddings)
- [ ] Reranking models
- [ ] Conversation memory
- [ ] Cloud deployment
