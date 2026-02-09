import os
import pdfplumber
from tqdm import tqdm

RAW_PDF_DIR = "data/raw_pdfs"
OUTPUT_DIR = "data/processed_docs/page_level"


def extract_pages_from_pdf(pdf_path: str, filename: str):
    """Extract text page-by-page and save each page separately."""
    pages = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if text and len(text.strip()) > 50:
                pages.append((page_num, text))

    return pages


def process_all_pdfs():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    pdf_files = [f for f in os.listdir(RAW_PDF_DIR) if f.endswith(".pdf")]

    for pdf_file in tqdm(pdf_files, desc="Extracting pages"):
        pdf_path = os.path.join(RAW_PDF_DIR, pdf_file)
        pages = extract_pages_from_pdf(pdf_path, pdf_file)

        for page_num, text in pages:
            output_filename = f"{pdf_file}_page_{page_num}.txt"
            output_path = os.path.join(OUTPUT_DIR, output_filename)

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)

    print("Page-level extraction complete!")


if __name__ == "__main__":
    process_all_pdfs()
