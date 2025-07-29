from fastapi import FastAPI, Request
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from typing import List

app = FastAPI()
model = SentenceTransformer("all-MiniLM-L6-v2")


class EmbedRequest(BaseModel):
    texts: List[str]


class EmbedResponse(BaseModel):
    vectors: List[List[float]]


@app.post("/embed", response_model=EmbedResponse)
def embed_texts(request: EmbedRequest):
    vectors = model.encode(request.texts).tolist()
    return {"vectors": vectors}
