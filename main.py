import json, uuid
from dataclasses import asdict, dataclass

@dataclass
class Message:
    id: str; sender: str; recipient: str; intent: str; payload: dict

def create(sender, recipient, intent, payload): return Message(str(uuid.uuid4()), sender, recipient, intent, payload)
def encode(message): return json.dumps(asdict(message))
def decode(raw): return Message(**json.loads(raw))

if __name__ == "__main__":
    msg = create("planner", "worker", "summarize", {"text": "Agents exchange structured messages."})
    print(decode(encode(msg)))
