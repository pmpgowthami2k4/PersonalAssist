
import os
from dotenv import load_dotenv
from groq import Groq

# from embeddings import get_embedding
# from vectorstore import collection
# from embeddings import get_embedding
# from vectorstore import collection


from embeddings import get_embedding
from vectorstore import collection


load_dotenv()


# GROQ CONFIG


GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not found in .env")

client = Groq(api_key=GROQ_API_KEY)

MODEL = "llama-3.1-8b-instant"


SYSTEM_PROMPT = (
    "You are a personal assistant that answers questions ONLY using the given context.\n"
    "The context comes from the user's personal documents (PDFs and text files).\n"
    "You MUST NOT use outside knowledge.\n"
    "If the answer is not present in the context, reply EXACTLY with:\n"
    "I don’t have that information in my knowledge base."
)


# RAG PIPELINE


# def generate_answer(query: str) -> str:
#     # 1. Embed the query
#     query_embedding = get_embedding(query)

#     # 2. Retrieve relevant chunks
#     results = collection.query(
#         query_embeddings=[query_embedding],
#         n_results=3
# )

#     docs = results.get("documents", [[]])[0]
#     ids = results.get("ids", [[]])[0]

#     print("\n🔍 QUERY:", query)
#     print("📄 RETRIEVED CHUNKS:")

#     for i, doc in enumerate(docs):
#         print(f"\n--- Chunk {i+1} (ID: {ids[i]}) ---")
#         print(doc[:300])  # print first 300 chars only


#     if not docs:
#         return "I don’t have that information in my knowledge base."

#     context = "\n".join(docs)

#     # 3. Generate answer with Groq
#     completion = client.chat.completions.create(
#         model=MODEL,
#         messages=[
#             {"role": "system", "content": SYSTEM_PROMPT},
#             {
#                 "role": "user",
#                 "content": f"Context:\n{context}\n\nQuestion:\n{query}"
#             }
#         ],
#         temperature=0.2,
#         max_tokens=512 #control response length
#     )

#     return completion.choices[0].message.content.strip()

def generate_answer(query: str) -> str:
    # 1. Embed the query
    query_embedding = get_embedding(query)

    # 2. Retrieve top-k chunks
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    ids = results.get("ids", [[]])[0]

    # DEBUG: PRINT RETRIEVAL DETAILS
 

    print("\n" + "=" * 60)
    print("🔍 QUERY:", query)
    print("📄 RETRIEVED CHUNKS:")

    for i in range(len(documents)):
        print(f"""
--- Result {i + 1} ---
Document ID : {metadatas[i].get('document_id')}
Chunk ID    : {metadatas[i].get('chunk_id')}
Source Type : {metadatas[i].get('source_type')}
Chunk Text  : {documents[i][:300]}...
""")

    print("=" * 60 + "\n")

    # 3. If nothing relevant found
    if not documents:
        return "I don’t have that information in my knowledge base."

    # 4. Build context
    context = "\n".join(documents)

    # 5. Generate answer with Groq
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:\n{query}"
            }
        ],
        temperature=0.1,
        max_tokens=120
    )

    return completion.choices[0].message.content.strip()