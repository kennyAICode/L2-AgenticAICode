import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ollama_http import generate


def classify(text: str) -> str:
    raw = generate(
        f"Request: {text}\nReply with exactly one label: QUESTION, TASK, or UNSAFE."
    ).upper()
    return next((label for label in ("UNSAFE", "QUESTION", "TASK") if label in raw), "QUESTION")


def run_workflow(text: str) -> str:
    route = classify(text)
    print("Selected edge:", route)
    if route == "UNSAFE":
        return "The request requires human review."
    if route == "TASK":
        return generate(f"Turn this task into three safe steps: {text}")
    return generate(f"Answer briefly for a beginner: {text}")


if __name__ == "__main__":
    print(run_workflow(input("Request: ")))

