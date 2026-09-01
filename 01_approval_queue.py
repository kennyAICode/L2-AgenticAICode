import json
import uuid
from datetime import datetime, timezone
from pathlib import Path


QUEUE = Path("approval_queue.json")


def load() -> list[dict]:
    return json.loads(QUEUE.read_text(encoding="utf-8")) if QUEUE.exists() else []


def submit(action: str, risk: str) -> dict:
    item = {"id": str(uuid.uuid4()), "action": action, "risk": risk, "status": "pending",
            "created_at": datetime.now(timezone.utc).isoformat()}
    items = load() + [item]
    QUEUE.write_text(json.dumps(items, indent=2), encoding="utf-8")
    return item


def decide(item_id: str, approved: bool, reviewer: str) -> None:
    items = load()
    for item in items:
        if item["id"] == item_id and item["status"] == "pending":
            item.update(status="approved" if approved else "rejected", reviewer=reviewer,
                        decided_at=datetime.now(timezone.utc).isoformat())
    QUEUE.write_text(json.dumps(items, indent=2), encoding="utf-8")


if __name__ == "__main__":
    pending = submit(input("Proposed action: "), input("Risk: "))
    print("Pending:", pending)
    decide(pending["id"], input("Approve? (yes/no): ").lower() == "yes", input("Reviewer: "))
    print(load()[-1])

