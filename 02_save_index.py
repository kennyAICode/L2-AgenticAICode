import json
from dataclasses import asdict
from pathlib import Path
from document_loader import ingest


if __name__ == "__main__":
    chunks = ingest()
    Path("chunks.json").write_text(
        json.dumps([asdict(chunk) for chunk in chunks], indent=2), encoding="utf-8"
    )
    print(f"Saved {len(chunks)} chunks to chunks.json")

