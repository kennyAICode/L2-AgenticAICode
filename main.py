import json
from dataclasses import asdict, dataclass
from pathlib import Path

@dataclass
class Persona: name:str; role:str; audience:str; tone:str; rules:list[str]
def validate(p):
    if not p.rules: raise ValueError("Persona needs rules")
    if p.audience not in {"beginner","manager","expert"}: raise ValueError("Unknown audience")
    return p
if __name__ == "__main__":
    p=validate(Persona("Maya","AI tutor","beginner","patient",["use simple words","give one example"])); Path("persona.json").write_text(json.dumps(asdict(p),indent=2)); print(p)
