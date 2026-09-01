import math
import re
from collections import Counter


def tokenize(text: str) -> list[str]:
    stop = {"a", "an", "and", "is", "of", "the", "to"}
    return [w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in stop]


def vector(text: str, documents: list[str]) -> dict[str, float]:
    terms = tokenize(text)
    counts = Counter(terms)
    result = {}
    for term, count in counts.items():
        containing = sum(term in tokenize(doc) for doc in documents)
        result[term] = count * (math.log((1 + len(documents)) / (1 + containing)) + 1)
    return result


def cosine(left: dict[str, float], right: dict[str, float]) -> float:
    dot = sum(value * right.get(term, 0) for term, value in left.items())
    a = math.sqrt(sum(value * value for value in left.values()))
    b = math.sqrt(sum(value * value for value in right.values()))
    return dot / (a * b) if a and b else 0.0


class VectorStore:
    def __init__(self, documents: list[str]):
        self.documents = documents
        self.vectors = [vector(doc, documents) for doc in documents]

    def search(self, query: str, top_k: int = 2) -> list[tuple[float, str]]:
        query_vector = vector(query, self.documents)
        scored = [(cosine(query_vector, item), doc) for item, doc in zip(self.vectors, self.documents)]
        return sorted(scored, reverse=True)[:top_k]

