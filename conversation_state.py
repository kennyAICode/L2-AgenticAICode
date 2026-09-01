from dataclasses import dataclass, field
from ollama_client import generate


@dataclass
class Message:
    role: str
    content: str


@dataclass
class AgentState:
    messages: list[Message] = field(default_factory=list)
    turn: int = 0

    def context(self, last_n: int = 6) -> str:
        return "\n".join(f"{m.role}: {m.content}" for m in self.messages[-last_n:])


def chat(state: AgentState, user_text: str) -> str:
    state.turn += 1
    state.messages.append(Message("User", user_text))
    answer = generate(
        "You are a concise tutor. Use the conversation context.\n"
        f"{state.context()}\nAssistant:"
    )
    state.messages.append(Message("Assistant", answer))
    return answer


if __name__ == "__main__":
    session = AgentState()
    while True:
        text = input("You: ").strip()
        if text.lower() == "quit":
            break
        print("Agent:", chat(session, text))
        print(f"[turn={session.turn}, messages={len(session.messages)}]")
