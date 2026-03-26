class MemoryStore:
    """
    Simple in-memory store (will upgrade to vector DB later)
    """

    def __init__(self):
        self.store = {}

    def save(self, key: str, value: str):
        self.store[key] = value

    def get(self, key: str):
        return self.store.get(key)

    def get_all(self):
        return self.store
