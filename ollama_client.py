import json
from urllib import request


def generate(prompt: str, model: str = "tinyllama") -> str:
    body = json.dumps({"model": model, "prompt": prompt, "stream": False}).encode()
    req = request.Request("http://localhost:11434/api/generate", data=body,
                          headers={"Content-Type": "application/json"})
    with request.urlopen(req, timeout=120) as response:
        return json.loads(response.read())["response"].strip()

