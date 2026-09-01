# L2 Day 16 — API Packaging and Containers

Expose TinyLlama through a validated FastAPI endpoint, test the health route and package the service in Docker.

```powershell
python -m pip install -r requirements.txt
uvicorn app:app --reload
pytest
docker build -t tinyllama-agent .
docker run -p 8000:8000 tinyllama-agent
```

Open `http://127.0.0.1:8000/docs`. Ollama must run on the host. Lab: add request IDs, timeouts, `/ready`, error tests and a non-root Docker user.

