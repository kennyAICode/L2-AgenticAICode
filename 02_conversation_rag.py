from rag import answer


if __name__ == "__main__":
    history = []
    while True:
        question = input("You: ").strip()
        if question.lower() == "quit":
            break
        expanded = question if not history else f"Previous topic: {history[-1]}\nCurrent: {question}"
        print("Agent:", answer(expanded))
        history.append(question)

