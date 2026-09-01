from ollama_client import OllamaClient


SYSTEM = """You are a concise classroom assistant. Answer in simple language.
If calculation is required, reply exactly as TOOL:calculator:<expression>.
Otherwise answer normally."""


def calculator(expression: str) -> str:
    allowed = set("0123456789+-*/(). ")
    if not expression or not set(expression) <= allowed:
        return "Invalid calculation"
    return str(eval(expression, {"__builtins__": {}}, {}))


def run_agent(question: str) -> str:
    llm = OllamaClient()
    decision = llm.generate(f"{SYSTEM}\nUser: {question}\nAssistant:")
    if decision.startswith("TOOL:calculator:"):
        expression = decision.split(":", 2)[2]
        observation = calculator(expression)
        return llm.generate(
            f"Question: {question}\nCalculation result: {observation}\nGive the final answer only."
        )
    return decision


if __name__ == "__main__":
    print("Simple Agent (type 'quit' to stop)")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            break
        print("Agent:", run_agent(user_input))

