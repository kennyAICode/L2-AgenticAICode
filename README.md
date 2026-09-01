# L2 Day 7 — Framework Capstone

This capstone combines state, planning, execution, checkpointing and human review.

## Run

```powershell
python capstone_agent.py
```

Run the automated test with `python -m unittest 02_tests.py`. The reusable module has no numeric prefix because Python module names cannot start with digits.

## Lab challenge

Add retries, restore from `checkpoint.json`, reject an empty plan, and revise rejected output once.
