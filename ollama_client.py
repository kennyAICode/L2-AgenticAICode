import json
from urllib import request


class OllamaClient:
    def __init__(self, model="tinyllama"):
        self.model = model

    def generate(self, prompt: str) -> str:
        data = json.dumps({"model": self.model, "prompt": prompt, "stream": False}).encode()
        req = request.Request("http://localhost:11434/api/generate", data=data,
                              headers={"Content-Type": "application/json"})
        with request.urlopen(req, timeout=120) as response:
            return json.loads(response.read())["response"].strip()

