import json
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ollama_http import generate


@dataclass
class AgentState:
    goal: str
    plan: list[str] = field(default_factory=list)
    outputs: list[str] = field(default_factory=list)
    status: str = "created"


def plan(state: AgentState) -> None:
    raw = generate(f"Goal: {state.goal}\nGive exactly 3 short numbered learning steps.")
    state.plan = [line.strip() for line in raw.splitlines() if line.strip()][:3]
    state.status = "planned"


def execute(state: AgentState) -> None:
    for step in state.plan:
        state.outputs.append(generate(f"Complete this step concisely: {step}"))
    state.status = "executed"


def checkpoint(state: AgentState) -> None:
    Path("checkpoint.json").write_text(json.dumps(asdict(state), indent=2), encoding="utf-8")


def review(state: AgentState) -> None:
    print("\n".join(state.outputs))
    state.status = "approved" if input("Approve? (yes/no): ").lower() == "yes" else "rejected"


if __name__ == "__main__":
    current = AgentState(input("Learning goal: "))
    for node in (plan, execute, checkpoint, review, checkpoint):
        print("Node:", node.__name__)
        node(current)
    print("Final status:", current.status)
