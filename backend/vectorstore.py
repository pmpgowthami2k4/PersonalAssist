# ChromaDB logic
# import chromadb

# client = chromadb.Client()
# collection = client.get_or_create_collection("personal_assistant")

# def store_chunks(chunks, embeddings):
#     ids = [f"chunk_{i}" for i in range(len(chunks))]
#     collection.add(
#         documents=chunks,
#         embeddings=embeddings,
#         ids=ids
#     )
import os
import chromadb

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_PATH = os.path.join(BASE_DIR, "chroma_db")

#  THIS IS THE IMPORTANT CHANGE
client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = client.get_or_create_collection("personal_assistant")

print("📦 Vectorstore path:", CHROMA_PATH)
print("📦 Vectorstore count:", collection.count())

