import json, shutil
from datetime import datetime, timezone
from pathlib import Path

RELEASES = Path("releases")

def release(version: str, config: dict) -> Path:
    target = RELEASES / version
    target.mkdir(parents=True, exist_ok=False)
    (target / "config.json").write_text(json.dumps(config, indent=2), encoding="utf-8")
    (target / "metadata.json").write_text(json.dumps({"version": version, "created": datetime.now(timezone.utc).isoformat()}), encoding="utf-8")
    Path("CURRENT").write_text(version, encoding="utf-8")
    return target

def rollback(version: str) -> None:
    if not (RELEASES / version).exists(): raise ValueError("Unknown release")
    Path("CURRENT").write_text(version, encoding="utf-8")

if __name__ == "__main__":
    RELEASES.mkdir(exist_ok=True)
    version = input("Version (example 1.0.0): ")
    print("Created", release(version, {"model": "tinyllama", "temperature": 0.2}))
    print("Current:", Path("CURRENT").read_text())
