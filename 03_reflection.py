from ollama_client import OllamaClient


def draft_and_refine(question: str) -> tuple[str, str, str]:
    llm = OllamaClient()
    draft = llm.generate(f"Answer for a beginner in at most 80 words: {question}")
    critique = llm.generate(
        f"Question: {question}\nDraft: {draft}\nList the single most important weakness."
    )
    final = llm.generate(
        f"Question: {question}\nDraft: {draft}\nCritique: {critique}\n"
        "Write an improved answer in at most 80 words."
    )
    return draft, critique, final


if __name__ == "__main__":
    d, c, f = draft_and_refine(input("Question: "))
    print("\nDRAFT\n", d, "\n\nCRITIQUE\n", c, "\n\nFINAL\n", f)

