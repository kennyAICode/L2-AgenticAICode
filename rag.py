import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ollama_client import generate


def words(text):
    return set(re.findall(r"[a-z0-9]+", text.lower())) - {"a", "an", "is", "the", "to"}


def answer(question: str) -> str:
    records = json.loads(Path("knowledge.json").read_text(encoding="utf-8"))
    sources = sorted(records, key=lambda x: len(words(question) & words(x["text"])), reverse=True)[:2]
    context = "\n".join(f'[{x["id"]}] {x["text"]}' for x in sources)
    return generate(f"Answer only from context and cite IDs.\n{context}\nQuestion: {question}")

