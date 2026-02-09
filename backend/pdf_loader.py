import fitz  # PyMuPDF
import os

def load_pdf_files(folder_path: str):
    """
    Loads all PDF files from a folder and returns
    a list of extracted text strings.
    """
    documents = []

    for file in os.listdir(folder_path):
        if file.lower().endswith(".pdf"):
            file_path = os.path.join(folder_path, file)

            doc = fitz.open(file_path)
            full_text = ""

            for page in doc:
                text = page.get_text()
                if text:
                    full_text += text + "\n"

            if full_text.strip():
                documents.append(full_text)

    return documents
