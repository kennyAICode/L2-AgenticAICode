import json
import os
from urllib import request
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(title="TinyLlama Agent API", version="1.0.0")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://host.docker.internal:11434")
MODEL = os.getenv("AGENT_MODEL", "tinyllama")


class AgentRequest(BaseModel):
    question: str = Field(min_length=1, max_length=1000)


class AgentResponse(BaseModel):
    answer: str
    model: str


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/ask", response_model=AgentResponse)
def ask(payload: AgentRequest):
    body = json.dumps({"model": MODEL, "prompt": payload.question, "stream": False}).encode()
    try:
        req = request.Request(f"{OLLAMA_URL}/api/generate", data=body,
                              headers={"Content-Type": "application/json"})
        with request.urlopen(req, timeout=120) as response:
            answer = json.loads(response.read())["response"].strip()
        return AgentResponse(answer=answer, model=MODEL)
    except Exception as exc:
        raise HTTPException(status_code=503, detail="Model service unavailable") from exc

