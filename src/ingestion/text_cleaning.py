import os
import re
from tqdm import tqdm

INPUT_DIR = "data/processed_docs/page_level"
CLEAN_DIR = "data/processed_docs/cleaned"


def split_into_sentences(text: str):
    """Basic sentence splitter using punctuation."""
    sentences = re.split(r'(?<=[.!?]) +', text)
    return [s.strip() for s in sentences if len(s.strip()) > 30]


def rebuild_paragraphs(text: str, sentences_per_paragraph=6):
    """Rebuild paragraphs from sentences."""
    sentences = split_into_sentences(text)
    paragraphs = []

    for i in range(0, len(sentences), sentences_per_paragraph):
        paragraph = " ".join(sentences[i:i + sentences_per_paragraph])
        paragraphs.append(paragraph)

    return "\n\n".join(paragraphs)


def clean_text(text: str):
    """Final production-grade cleaning pipeline."""

    # Fix spaced uppercase titles like "C E N T R E"
    text = re.sub(
        r"\b(?:[A-Z]\s){2,}[A-Z]\b",
        lambda m: m.group(0).replace(" ", ""),
        text
    )

    # Remove page number patterns like "4 5"
    text = re.sub(r"\b\d+\s+\d+\b", " ", text)

    # Remove standalone numbers
    text = re.sub(r"\n\s*\d+\s*\n", "\n", text)

    # Remove "Page X"
    text = re.sub(r"Page\s*\d+", "", text, flags=re.IGNORECASE)

    # Replace ALL newlines with space (reset formatting)
    text = text.replace("\n", " ")

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    # 🔥 Rebuild paragraphs from sentences
    text = rebuild_paragraphs(text)

    return text.strip()


def clean_all_documents():
    os.makedirs(CLEAN_DIR, exist_ok=True)

    txt_files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".txt")]

    for file in tqdm(txt_files, desc="Cleaning documents"):
        path = os.path.join(INPUT_DIR, file)

        with open(path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        cleaned_text = clean_text(raw_text)

        output_path = os.path.join(CLEAN_DIR, file)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(cleaned_text)

    print("Text cleaning completed!")


if __name__ == "__main__":
    clean_all_documents()
