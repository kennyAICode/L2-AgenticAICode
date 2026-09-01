import json
from dataclasses import asdict
from pathlib import Path
from conversation_state import AgentState, Message


CHECKPOINT = Path("agent_state.json")


def save_state(state: AgentState) -> None:
    CHECKPOINT.write_text(json.dumps(asdict(state), indent=2), encoding="utf-8")


def load_state() -> AgentState:
    if not CHECKPOINT.exists():
        return AgentState()
    raw = json.loads(CHECKPOINT.read_text(encoding="utf-8"))
    return AgentState(
        messages=[Message(**item) for item in raw["messages"]],
        turn=raw["turn"],
    )


if __name__ == "__main__":
    state = load_state()
    state.messages.append(Message("User", "Remember that my preferred language is Python."))
    state.turn += 1
    save_state(state)
    print("Saved:", CHECKPOINT.resolve())
