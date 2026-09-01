from ollama_client import OllamaClient


def observe() -> str:
    return input("Goal: ").strip()


def decide(llm: OllamaClient, goal: str) -> str:
    prompt = f"""Goal: {goal}
Choose one action: EXPLAIN, CALCULATE, or STOP.
Return only ACTION: value. Use STOP for an empty goal."""
    return llm.generate(prompt)


def act(action: str, goal: str) -> str:
    if "STOP" in action:
        return "Stopping"
    if "CALCULATE" in action:
        return f"A calculator tool should handle: {goal}"
    return f"The explanation tool should handle: {goal}"


if __name__ == "__main__":
    client = OllamaClient()
    goal = observe()
    selected_action = decide(client, goal)
    print("Decision:", selected_action)
    print("Result:", act(selected_action, goal))

