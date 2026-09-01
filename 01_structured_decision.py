import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ollama_http import generate


@dataclass
class Decision:
    intent: str
    confidence: float
    reason: str


def extract_json(text: str) -> dict:
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON object returned")
    return json.loads(match.group())


def infer(request: str) -> Decision:
    prompt = f"""Request: {request}
Classify intent as explain, calculate, or unknown.
Return JSON only: {{"intent":"...","confidence":0.0,"reason":"..."}}"""
    try:
        data = extract_json(generate(prompt, temperature=0.0))
        intent = data.get("intent", "unknown")
        if intent not in {"explain", "calculate", "unknown"}:
            intent = "unknown"
        return Decision(intent, max(0.0, min(1.0, float(data.get("confidence", 0)))), str(data.get("reason", "")))
    except (ValueError, TypeError, json.JSONDecodeError):
        return Decision("unknown", 0.0, "Model output could not be validated")


if __name__ == "__main__":
    print(infer(input("Request: ")))

