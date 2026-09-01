import re
from pathlib import Path


def tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def retrieve(question: str, top_k: int = 2) -> list[str]:
    passages = Path("knowledge.txt").read_text(encoding="utf-8").splitlines()
    query_words = tokens(question)
    scored = [(len(query_words & tokens(passage)), passage) for passage in passages if passage.strip()]
    return [passage for score, passage in sorted(scored, reverse=True)[:top_k] if score > 0]


if __name__ == "__main__":
    for result in retrieve(input("Question: ")):
        print("-", result)

