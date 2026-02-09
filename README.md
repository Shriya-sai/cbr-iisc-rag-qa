
```mermaid
flowchart LR
    A[User Question] --> B[Retriever<br/>FAISS Vector DB]
    B --> C[Relevant Document Chunks]
    C --> D[Prompt Builder]
    D --> E[Local LLM<br/>Mistral via Ollama]
    E --> F[Answer + Citations]
