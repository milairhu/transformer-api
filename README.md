# 🚀 Embedding API – MiniLM-L6-v2

This is a lightweight Python API that exposes a REST endpoint to generate sentence embeddings using the all-MiniLM-L6-v2 model from Sentence Transformers.

## 🧠 What it does

It exposes a single POST endpoint /embed that takes a list of input texts and returns their vector representations, ready to be stored or queried against a vector database like Qdrant.

## ▶️ Quickstart

Build and run the API in Docker:

docker build -t transformer-api .
docker run -d --name transformer-api -p 8000:8000 transformer-api

The API will now be available at http://localhost:8000/embed

## 🧪 Usage

Make a POST request to the /embed endpoint:

curl -X POST http://localhost:8000/embed \
-H "Content-Type: application/json" \
-d '{"texts": ["What are your data retention policies?"]}'

Example response:

{
"vectors": [
[0.123, -0.456, 0.789, ...]  // Vector of floats
]
}