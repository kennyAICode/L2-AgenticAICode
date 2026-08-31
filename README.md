# L2 Day 1 — Agentic AI Foundations

## Learning outcomes

- Distinguish a chatbot from an agent.
- Implement the observe → decide → act loop.
- Let TinyLlama select a calculator tool.
- Apply a basic safety restriction instead of evaluating arbitrary Python.

## Setup on Windows

```powershell
ollama serve
ollama pull tinyllama
python 01_simple_agent.py
python 02_agent_loop.py
```

No third-party Python package is required. Keep `ollama_client.py` in this folder.

## Lab

1. Ask `What is 125 * 8?` and observe the tool call.
2. Ask a factual question and observe the direct LLM response.
3. Add a `word_count` tool and teach the prompt to select it.

## Teaching note

TinyLlama may not follow the tool format every time. This is useful for discussing validation, retries, constrained output and why production agents need control code.

