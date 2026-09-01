# L2 Day 5 — Routing, Retry and Conditional Workflows

## Learning outcomes

- Route requests through conditional branches.
- Retry transient failures with a small backoff.
- Return a safe fallback when retries are exhausted.
- Pause a workflow for human review and revision.

## Run

```powershell
python 01_router.py
python 02_retry_fallback.py
python 03_workflow.py
```

## Lab

1. Add a `SUMMARIZE` route.
2. Retry only connection failures, not every exception.
3. Store the workflow state in JSON.
4. Limit revision to two cycles to prevent an infinite loop.

