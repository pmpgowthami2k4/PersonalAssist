import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Embeddings MUST use OpenRouter / OpenAI-compatible key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("❌ OPENROUTER_API_KEY not found in environment")

EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_URL = "https://openrouter.ai/api/v1/embeddings"

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://github.com/pmpgowthami2k4/PersonalAssist",
    "X-Title": "Personal Assistant"
}

def get_embedding(text: str):
    payload = {
        "model": EMBEDDING_MODEL,
        "input": text
    }

    response = requests.post(
        EMBEDDING_URL,
        headers=HEADERS,
        json=payload,
        timeout=30
    )

    if response.status_code != 200:
        raise Exception(f"Embedding error: {response.text}")

    return response.json()["data"][0]["embedding"]
