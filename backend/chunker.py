# def chunk_text(text, chunk_size=600, overlap=100):
#     chunks = []
#     start = 0

#     while start < len(text):
#         end = start + chunk_size
#         chunks.append(text[start:end])
#         start += chunk_size - overlap

#     return chunks

# import tiktoken


# def token_chunker(text, chunk_size=500, overlap=100):
#     """
#     Token-based chunking using OpenAI-compatible tokenizer.
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


# import os
# import tiktoken



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



# def token_chunker(text, chunk_size=500, overlap=100):
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

import tiktoken


def chunk_text(text, chunk_size=500, overlap=100):
    """
    Token-based chunking using OpenAI tokenizer.
    """

    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)

    chunks = []
    start = 0

    while start < len(tokens):
        end = start + chunk_size
        chunk = enc.decode(tokens[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks

