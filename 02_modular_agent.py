from dataclasses import dataclass
from ollama_client import generate
from tool_registry import ToolRegistry, uppercase, word_count


@dataclass
class AgentResult:
    input_text: str
    decision: str
    output: str


class ClassroomAgent:
    def __init__(self):
        self.tools = ToolRegistry()
        self.tools.register("uppercase", uppercase)
        self.tools.register("word_count", word_count)

    def run(self, user_input: str) -> AgentResult:
        decision = generate(
            f"Input: {user_input}\nChoose a tool from {self.tools.names()}. "
            "Reply with only the tool name."
        ).lower()
        chosen = next((name for name in self.tools.names() if name in decision), "word_count")
        output = self.tools.execute(chosen, user_input)
        return AgentResult(user_input, chosen, output)


if __name__ == "__main__":
    result = ClassroomAgent().run(input("Text: "))
    print(result)
