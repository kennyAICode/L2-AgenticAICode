from dataclasses import dataclass
from ollama_client import generate


@dataclass
class WorkflowState:
    topic: str
    draft: str = ""
    approved: bool = False


def create_draft(state: WorkflowState) -> None:
    state.draft = generate(f"Write a two-sentence beginner note about {state.topic}.")


def human_review(state: WorkflowState) -> None:
    print("\nDRAFT:\n", state.draft)
    state.approved = input("Approve? (yes/no): ").strip().lower() == "yes"


def revise(state: WorkflowState) -> None:
    feedback = input("Revision instruction: ")
    state.draft = generate(f"Draft: {state.draft}\nFeedback: {feedback}\nRevise it.")


if __name__ == "__main__":
    workflow = WorkflowState(input("Topic: "))
    create_draft(workflow)
    human_review(workflow)
    if not workflow.approved:
        revise(workflow)
    print("\nFINAL:\n", workflow.draft)

