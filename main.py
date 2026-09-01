from dataclasses import dataclass

@dataclass(frozen=True)
class Model: name: str; max_chars: int; priority: int
MODELS=[Model("tinyllama",1000,1), Model("llama3.2:1b",4000,2)]
def route(prompt):
    candidates=[m for m in MODELS if len(prompt)<=m.max_chars]
    if not candidates: raise ValueError("Prompt too large")
    return min(candidates,key=lambda m:m.priority)

if __name__ == "__main__": print("Selected:", route(input("Prompt: ")).name)
