from dataclasses import dataclass

@dataclass
class Tool: name: str; keywords: set[str]; function: object; approval: bool = False
TOOLS = [Tool("count", {"count", "words"}, lambda x: len(x.split())), Tool("uppercase", {"upper", "uppercase"}, str.upper), Tool("send", {"send", "message"}, lambda x: f"SENT: {x}", True)]

def run(goal: str):
    words = set(goal.lower().split()); tool = max(TOOLS, key=lambda t: len(words & t.keywords))
    if tool.approval and input(f"Approve {tool.name}? (yes/no): ").lower() != "yes": return "Rejected"
    return tool.function(goal)

if __name__ == "__main__": print(run(input("Goal: ")))
