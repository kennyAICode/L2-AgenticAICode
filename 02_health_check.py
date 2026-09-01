import json
from urllib import error, request
from config import settings


def check_ollama() -> dict:
    try:
        with request.urlopen(f"{settings.ollama_url}/api/tags", timeout=3) as response:
            models = [item["name"] for item in json.loads(response.read()).get("models", [])]
            return {"status": "healthy", "model_available": any(settings.model in name for name in models)}
    except (error.URLError, TimeoutError) as exc:
        return {"status": "unhealthy", "error": str(exc)}


if __name__ == "__main__":
    print(json.dumps(check_ollama(), indent=2))

