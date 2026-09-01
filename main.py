from dataclasses import dataclass

@dataclass(frozen=True)
class ToolCard:
    name: str; tags: tuple[str, ...]; cost: int; risk: int

TOOLS = [ToolCard("calculator", ("math", "number"), 1, 1), ToolCard("notes_search", ("search", "notes"), 2, 1), ToolCard("email", ("send", "message"), 4, 5)]

def discover(goal: str):
    words = set(goal.lower().split())
    return sorted(TOOLS, key=lambda t: (-len(words & set(t.tags)), t.risk, t.cost))

if __name__ == "__main__":
    for item in discover(input("Goal: ")): print(item)
