from dataclasses import dataclass

@dataclass
class AddInput:
    a: float; b: float

def validate(data: dict) -> AddInput:
    unknown = set(data) - {"a", "b"}
    if unknown: raise ValueError(f"Unknown fields: {unknown}")
    try: return AddInput(float(data["a"]), float(data["b"]))
    except (KeyError, TypeError, ValueError) as exc: raise ValueError("a and b must be numbers") from exc

def add(data: dict) -> float:
    item = validate(data); return item.a + item.b

if __name__ == "__main__":
    print(add({"a": input("a: "), "b": input("b: ")}))
