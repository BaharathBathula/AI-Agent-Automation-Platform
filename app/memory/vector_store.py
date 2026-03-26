import math


class SimpleVectorStore:
    """
    Basic vector store (simulation for RAG)
    """

    def __init__(self):
        self.vectors = []

    def embed(self, text: str):
        # Fake embedding (replace later with OpenAI embeddings)
        return [len(text), sum(ord(c) for c in text) % 1000]

    def add(self, text: str):
        embedding = self.embed(text)
        self.vectors.append((text, embedding))

    def similarity(self, v1, v2):
        return sum(a * b for a, b in zip(v1, v2))

    def search(self, query: str, top_k: int = 3):
        query_vec = self.embed(query)

        scored = [
            (text, self.similarity(query_vec, emb))
            for text, emb in self.vectors
        ]

        scored.sort(key=lambda x: x[1], reverse=True)

        return [text for text, _ in scored[:top_k]]
