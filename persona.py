import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ollama_http import generate


@dataclass(frozen=True)
class Persona:
    name: str
    role: str
    tone: str
    rules: tuple[str, ...]

    def system_prompt(self) -> str:
        rules = "\n".join(f"- {rule}" for rule in self.rules)
        return f"Name: {self.name}\nRole: {self.role}\nTone: {self.tone}\nRules:\n{rules}"


TUTOR = Persona(
    name="Maya",
    role="beginner Python tutor",
    tone="patient, encouraging and concise",
    rules=("Use simple words", "Give one small example", "Do not invent facts"),
)


def respond(persona: Persona, question: str) -> str:
    return generate(f"{persona.system_prompt()}\nLearner: {question}\n{persona.name}:")


if __name__ == "__main__":
    print(respond(TUTOR, input("Question: ")))
