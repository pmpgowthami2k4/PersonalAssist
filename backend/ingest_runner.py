
# from ingest import load_txt_files
# from pdf_loader import load_pdf_files
# from chunker import chunk_text
# from embeddings import get_embedding
# from vectorstore import collection

# def ingest():
#     folder_path = "../data/documents"

#     # 1. Load TXT and PDF files
#     txt_docs = load_txt_files(folder_path)
#     pdf_loader = load_pdf_files(folder_path)

#     documents = txt_docs + pdf_loader

#     if not documents:
#         raise RuntimeError("❌ No TXT or PDF documents found.")

#     all_chunks = []
#     all_embeddings = []

#     # 2. Chunk + embed
#     for doc in documents:
#         chunks = chunk_text(doc)
#         for chunk in chunks:
#             all_chunks.append(chunk)
#             all_embeddings.append(get_embedding(chunk))

#     # 3. Store in Chroma
#     ids = [f"chunk_{i}" for i in range(len(all_chunks))]

#     collection.add(
#         documents=all_chunks,
#         embeddings=all_embeddings,
#         ids=ids
#     )

#     print(f"✅ Ingestion complete. Stored {len(all_chunks)} chunks.")

# if __name__ == "__main__":
#     ingest()
import os
from ingest import load_txt_files
from pdf_loader import load_pdf_files
from chunker import chunk_text
from embeddings import get_embedding
from vectorstore import collection


def ingest():
    folder_path = "../data/documents"

    all_chunks = []
    all_embeddings = []
    all_metadatas = []
    all_ids = []

    # -------- TXT FILES --------
    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            file_path = os.path.join(folder_path, file)
            documents = load_txt_files(folder_path)

            for doc_index, doc in enumerate(documents):
                chunks = chunk_text(doc)

                for i, chunk in enumerate(chunks):
                    chunk_id = f"{file}_chunk_{i}"

                    all_chunks.append(chunk)
                    all_embeddings.append(get_embedding(chunk))
                    all_ids.append(chunk_id)
                    all_metadatas.append({
                        "document_id": file,
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


if __name__ == "__main__":
    ingest()
