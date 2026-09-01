from dataclasses import dataclass
from collections.abc import Callable

@dataclass(frozen=True)
class Tool:
    name: str; description: str; function: Callable[[str], str]

class Registry:
    def __init__(self): self.tools = {}
    def register(self, tool: Tool):
        if tool.name in self.tools: raise ValueError("Duplicate tool")
        self.tools[tool.name] = tool
    def discover(self, words: str):
        query = set(words.lower().split())
        return sorted(self.tools.values(), key=lambda t: len(query & set(t.description.lower().split())), reverse=True)

if __name__ == "__main__":
    r = Registry(); r.register(Tool("uppercase", "convert text to uppercase", str.upper)); r.register(Tool("count", "count words in text", lambda x: str(len(x.split()))))
    for tool in r.discover(input("Need: ")): print(tool.name, "-", tool.description)
