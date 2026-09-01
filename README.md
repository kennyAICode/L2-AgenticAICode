# L2 Day 4 — State Management and Checkpoints

## Concepts

- State carries data between agent steps.
- Short-term memory is selected conversation context.
- A checkpoint makes state recoverable after the program stops.
- Dataclasses make the state schema explicit.

## Run

```powershell
python conversation_state.py
python 02_json_checkpoint.py
```

## Lab

1. Add a `user_name` field to `AgentState`.
2. Save after every conversation turn.
3. Add a `clear` command that resets state only after confirmation.
4. Do not commit `agent_state.json` when it contains personal information.
