import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ollama_client import generate


def words(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower())) - {"a", "an", "is", "the", "to"}


def retrieve(question: str, top_k: int = 2) -> list[dict]:
    records = json.loads(Path("knowledge.json").read_text(encoding="utf-8"))
    return sorted(records, key=lambda item: len(words(question) & words(item["text"])), reverse=True)[:top_k]


def answer(question: str) -> str:
    sources = retrieve(question)
    context = "\n".join(f'[{item["id"]}] {item["text"]}' for item in sources)
    return generate(
        f"Use only these sources. Cite source IDs in square brackets. "
        f"If insufficient, say so.\n{context}\nQuestion: {question}\nAnswer:"
    )


if __name__ == "__main__":
    print(answer(input("Question: ")))

