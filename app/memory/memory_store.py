from app.memory.vector_store import SimpleVectorStore


class MemoryStore:

    def __init__(self):
        self.kv_store = {}
        self.vector_store = SimpleVectorStore()

    def save(self, key: str, value: str):
        self.kv_store[key] = value
        self.vector_store.add(value)

    def get(self, key: str):
        return self.kv_store.get(key)

    def search(self, query: str):
        return self.vector_store.search(query)
