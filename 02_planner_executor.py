from ollama_client import OllamaClient


def make_plan(goal: str) -> list[str]:
    response = OllamaClient().generate(
        f"Goal: {goal}\nCreate exactly 3 short steps, one per line, numbered 1 to 3."
    )
    lines = [line.strip() for line in response.splitlines() if line.strip()]
    return lines[:3]


def execute(step: str) -> str:
    return OllamaClient().generate(f"Perform this learning-plan step briefly: {step}")


if __name__ == "__main__":
    plan = make_plan(input("Learning goal: "))
    for number, step in enumerate(plan, 1):
        print(f"\nStep {number}: {step}")
        print("Output:", execute(step))

