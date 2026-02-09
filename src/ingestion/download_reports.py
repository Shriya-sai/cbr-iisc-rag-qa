import os
import requests

SAVE_DIR = "data/raw_pdfs"

REPORT_URLS = {
    "2024-25": "https://cbr-iisc.ac.in/wp-content/uploads/2025/12/CBR-annual-report_upload.pdf",
    "2023-24": "https://cbr-iisc.ac.in/wp-content/uploads/2025/03/Annual-report-2023-24.pdf",
    "2022-23": "https://cbr-iisc.ac.in/wp-content/uploads/2024/08/CBR-Annual-Report-2022-23.pdf",
}


def download_pdf(year, url):
    filename = f"CBR_Annual_Report_{year}.pdf"
    filepath = os.path.join(SAVE_DIR, filename)

    if os.path.exists(filepath):
        print(f"Already exists: {filename}")
        return

    print(f"Downloading {filename}...")
    response = requests.get(url)

    with open(filepath, "wb") as f:
        f.write(response.content)


def main():
    os.makedirs(SAVE_DIR, exist_ok=True)

    for year, url in REPORT_URLS.items():
        download_pdf(year, url)

    print("Download complete!")


if __name__ == "__main__":
    main()
