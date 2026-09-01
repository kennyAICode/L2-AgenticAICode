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
    words, chunks, start = text.split(), [], 0
    while start < len(words):
        chunks.append(" ".join(words[start:start + size]))
        start += size - overlap
    return chunks


def ingest(folder: str = "documents") -> list[Chunk]:
    output = []
    for path in sorted(Path(folder).glob("*.txt")):
        for number, text in enumerate(chunk_words(path.read_text(encoding="utf-8")), 1):
            output.append(Chunk(path.name, number, text))
    return output


if __name__ == "__main__":
    for chunk in ingest():
        print(chunk)

