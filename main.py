import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ollama_client import generate

class Gateway:
    def complete(self, model, prompt):
        provider, name = model.split("/",1)
        if provider != "ollama": raise ValueError("Unsupported provider")
        return generate(prompt, model=name)

if __name__ == "__main__": print(Gateway().complete("ollama/tinyllama", input("Prompt: ")))
