
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

# import os
# import tiktoken


# # ----------------------------------
# # Load TXT Files
# # ----------------------------------

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


# # ----------------------------------
# # Token-Based Chunker
# # ----------------------------------

# def chunk_text(text, chunk_size=500, overlap=100):
#     """
#     Splits text into token-based chunks using tiktoken.
#     """

#     enc = tiktoken.get_encoding("cl100k_base")
#     tokens = enc.encode(text)

#     chunks = []
#     start = 0

#     while start < len(tokens):
#         end = start + chunk_size
#         chunk = enc.decode(tokens[start:end])
#         chunks.append(chunk)
#         start += chunk_size - overlap

#     return chunks

from ingest import ingest

if __name__ == "__main__":
    ingest()