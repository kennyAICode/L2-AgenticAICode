from structured_decision import infer


def safe_calculate(text: str) -> str:
    expression = "".join(c for c in text if c in "0123456789+-*/(). ")
    return str(eval(expression, {"__builtins__": {}}, {})) if expression.strip() else "No expression"


def execute(request: str) -> str:
    decision = infer(request)
    print("Inference:", decision)
    if decision.confidence < 0.65 or decision.intent == "unknown":
        return "Please clarify the request; confidence is too low."
    if decision.intent == "calculate":
        return safe_calculate(request)
    return "The explain action would now call the tutor persona."


if __name__ == "__main__":
    print(execute(input("Request: ")))
