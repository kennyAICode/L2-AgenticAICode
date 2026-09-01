# L2 Day 2 — Agentic Design Patterns

This day implements three foundational patterns: ReAct-style reasoning/action/observation, planner–executor, and reflection.

## Run

```powershell
ollama serve
python 01_react_agent.py
python 02_planner_executor.py
python 03_reflection.py
```

## Lab exercises

1. Add two entries to the ReAct agent's knowledge dictionary.
2. Change the planner from three steps to five and validate the result.
3. Make the reflector score the draft from 1–5 before rewriting it.
4. Record where TinyLlama fails to follow a requested output format.

