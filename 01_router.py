from ollama_client import generate


def calculate(text: str) -> str:
    expression = "".join(c for c in text if c in "0123456789+-*/(). ")
    if not expression.strip():
        return "No valid expression found."
    return str(eval(expression, {"__builtins__": {}}, {}))


def explain(text: str) -> str:
    return generate(f"Explain this to a beginner in at most 60 words: {text}")


def route(text: str) -> str:
    decision = generate(
        f"Request: {text}\nClassify it. Reply only CALCULATE or EXPLAIN."
    ).upper()
    return calculate(text) if "CALCULATE" in decision else explain(text)


if __name__ == "__main__":
    print(route(input("Request: ")))

