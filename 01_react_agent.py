from ollama_client import OllamaClient


KNOWLEDGE = {
    "python": "Python is a readable general-purpose programming language.",
    "ollama": "Ollama runs supported language models locally.",
    "agent": "An agent observes, decides, acts and evaluates the result.",
}


def search_notes(query: str) -> str:
    query = query.lower()
    matches = [text for key, text in KNOWLEDGE.items() if key in query]
    return " ".join(matches) or "No matching classroom note."


def react(question: str) -> str:
    llm = OllamaClient()
    thought = llm.generate(
        f"Question: {question}\nDecide whether classroom notes are needed. "
        "Reply only SEARCH:<keywords> or ANSWER:<answer>."
    )
    print("Reason/Action:", thought)
    if thought.startswith("SEARCH:"):
        observation = search_notes(thought.split(":", 1)[1])
        print("Observation:", observation)
        return llm.generate(f"Question: {question}\nNotes: {observation}\nFinal concise answer:")
    return thought.removeprefix("ANSWER:").strip()


if __name__ == "__main__":
    print(react(input("Question: ")))

