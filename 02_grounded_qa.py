import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ollama_http import generate
from keyword_retriever import retrieve


def answer(question: str) -> str:
    passages = retrieve(question)
    if not passages:
        return "I could not find this in the approved knowledge base."
    context = "\n".join(passages)
    draft = generate(
        f"Use only the context. If insufficient, say so.\nContext:\n{context}\nQuestion: {question}"
    )
    print("\nSOURCE CONTEXT:\n", context)
    print("\nDRAFT:\n", draft)
    return draft if input("Approve answer? (yes/no): ").lower() == "yes" else "Answer withheld for review."


if __name__ == "__main__":
    print("\nFINAL:\n", answer(input("Question: ")))
