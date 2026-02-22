# # FastAPI entry point
# from fastapi import FastAPI
# from pydantic import BaseModel
# from rag import generate_answer
# import uvicorn


# # FASTAPI APP


# app = FastAPI(
#     title="RAG Personal Assistant",
#     description="Gemini-powered RAG assistant",
#     version="1.0"
# )

# # REQUEST / RESPONSE MODELS

# class ChatRequest(BaseModel):
#     query: str


# class ChatResponse(BaseModel):
#     answer: str


# # CHAT ENDPOINT


# # @app.post("/chat", response_model=ChatResponse)
# # def chat(request: ChatRequest):
# #     """
# #     Receives user query and returns RAG-based answer.
# #     """
# #     answer = generate_answer(request.query)
# #     return {"answer": answer}

# @app.post("/chat")
# def chat(req: ChatRequest):
#     try:
#         answer = generate_answer(req.query)
#         return {"answer": answer}
#     except Exception as e:
#         print("❌ ERROR:", e)
#         raise


# # HEALTH CHECK (OPTIONAL)

# @app.get("/")
# def health():
#     return {"status": "RAG assistant is running"}

# # RUN SERVER


# if __name__ == "__main__":
#     uvicorn.run(
#         "main:app",
#         host="127.0.0.1",
#         port=8000,
#         reload=True
#     )

# FastAPI entry point

from fastapi import FastAPI
from pydantic import BaseModel
# from backend.rag import generate_answer
from rag import generate_answer



# FASTAPI APP

app = FastAPI(
    title="RAG Personal Assistant",
    description="Groq-powered RAG assistant",
    version="1.0"
)



# REQUEST / RESPONSE MODELS


class ChatRequest(BaseModel):
    query: str


class ChatResponse(BaseModel):
    answer: str



# CHAT ENDPOINT

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    try:
        answer = generate_answer(req.query)
        return {"answer": answer}
    except Exception as e:
        print("❌ ERROR:", e)
        raise

# HEALTH CHECK

@app.get("/")
def health():
    return {"status": "RAG assistant is running"}
