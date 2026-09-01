import json
from urllib import request, error


class OllamaClient:
    def __init__(self, model="tinyllama", base_url="http://localhost:11434"):
        self.model = model
        self.url = f"{base_url}/api/generate"

    def generate(self, prompt: str, temperature: float = 0.2) -> str:
        payload = json.dumps({
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": temperature},
        }).encode()
        req = request.Request(self.url, data=payload, headers={"Content-Type": "application/json"})
        try:
            with request.urlopen(req, timeout=120) as response:
                return json.loads(response.read())["response"].strip()
        except error.URLError as exc:
            raise RuntimeError("Ollama is unavailable. Run: ollama serve") from exc

