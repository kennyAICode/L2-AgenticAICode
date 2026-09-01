import time
from ollama_client import generate


def reliable_generate(prompt: str, attempts: int = 3) -> str:
    last_error = None
    for attempt in range(1, attempts + 1):
        try:
            print(f"Attempt {attempt}/{attempts}")
            answer = generate(prompt)
            if answer:
                return answer
            raise ValueError("The model returned an empty response")
        except Exception as exc:
            last_error = exc
            if attempt < attempts:
                time.sleep(attempt)
    return f"Fallback response: service unavailable ({last_error})"


if __name__ == "__main__":
    print(reliable_generate("Give one sentence explaining an AI agent."))

