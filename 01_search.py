from tfidf_store import VectorStore


DOCUMENTS = [
    "Python functions are declared using the def keyword.",
    "Agent state carries information between workflow nodes.",
    "Human approval can stop a risky agent action.",
    "Ollama runs language models on a local computer.",
]


if __name__ == "__main__":
    store = VectorStore(DOCUMENTS)
    for score, document in store.search(input("Search: ")):
        print(f"{score:.3f} | {document}")

