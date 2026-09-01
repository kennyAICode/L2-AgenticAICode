from dataclasses import dataclass
from pathlib import Path


@dataclass
class Chunk:
    source: str
    number: int
    text: str


def chunk_words(text: str, size: int = 12, overlap: int = 3) -> list[str]:
    if size <= overlap:
        raise ValueError("size must be greater than overlap")
    words, result, start = text.split(), [], 0
    while start < len(words):
        result.append(" ".join(words[start:start + size]))
        start += size - overlap
    return result


def ingest(folder: str = "documents") -> list[Chunk]:
    return [Chunk(path.name, n, text)
            for path in sorted(Path(folder).glob("*.txt"))
            for n, text in enumerate(chunk_words(path.read_text(encoding="utf-8")), 1)]

