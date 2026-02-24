# import os

# def load_txt_files(folder_path):
#     texts = []

#     for file in os.listdir(folder_path):
#         if file.endswith(".txt"):
#             file_path = os.path.join(folder_path, file)
#             with open(file_path, "r", encoding="utf-8") as f:
#                 content = f.read().strip()
#                 if content:
#                     texts.append(content)

#     return texts


import os
# from chunker import chunk_text
# from embeddings import get_embedding
# from vectorstore import collection
from chunker import chunk_text
from embeddings import get_embedding
from vectorstore import BASE_DIR, collection

from pdf_loader import load_pdf_files


def load_txt_files(folder_path):
    texts = []

    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            file_path = os.path.join(folder_path, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    texts.append((file, content))

    return texts


# def ingest():
#     BASE_DIR = os.path.dirname(__file__)
#     folder_path = os.path.join(BASE_DIR, "data", "documents")

#     print("📂 Loading from:", folder_path)

#     all_chunks = []
#     all_embeddings = []
#     all_ids = []
#     all_metadatas = []

def ingest():
    print("🚀 INGEST FUNCTION STARTED")

    BASE_DIR = os.path.dirname(__file__)
    folder_path = os.path.join(BASE_DIR, "data", "documents")

    print("📂 Loading from:", folder_path)

    if not os.path.exists(folder_path):
        print("❌ Folder does not exist!")
        raise RuntimeError("Documents folder not found")

    print("📄 Files found:", os.listdir(folder_path))

    # -------- TXT FILES --------
    txt_files = load_txt_files(folder_path)

    for file_name, text in txt_files:
        chunks = chunk_text(text)

        for i, chunk in enumerate(chunks):
            chunk_id = f"{file_name}_chunk_{i}"

            all_chunks.append(chunk)
            all_embeddings.append(get_embedding(chunk))
            all_ids.append(chunk_id)
            all_metadatas.append({
                "document_id": file_name,
                "chunk_id": chunk_id,
                "source_type": "txt"
            })

    # -------- PDF FILES --------
    pdf_texts = load_pdf_files(folder_path)
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]

    for pdf_file, pdf_text in zip(pdf_files, pdf_texts):
        chunks = chunk_text(pdf_text)

        for i, chunk in enumerate(chunks):
            chunk_id = f"{pdf_file}_chunk_{i}"

            all_chunks.append(chunk)
            all_embeddings.append(get_embedding(chunk))
            all_ids.append(chunk_id)
            all_metadatas.append({
                "document_id": pdf_file,
                "chunk_id": chunk_id,
                "source_type": "pdf"
            })

    if not all_chunks:
        raise RuntimeError("No documents found to ingest.")

    collection.add(
        documents=all_chunks,
        embeddings=all_embeddings,
        ids=all_ids,
        metadatas=all_metadatas
    )

    print(f"✅ Ingestion complete. Stored {len(all_chunks)} chunks.")
