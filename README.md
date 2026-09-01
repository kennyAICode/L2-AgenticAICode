# L2 Day 3 — Programming Framework: Anatomy and Tool Registry

The examples separate model access, tool registration, orchestration and result data. This modular structure is the beginning of an agent framework.

## Run

```powershell
python tool_registry.py
python 02_modular_agent.py
```

The reusable registry module has no numeric prefix because Python importable module names cannot begin with a digit.

## Lab

- Add `lowercase` and `character_count` tools.
- Reject duplicate tool names.
- Add descriptions to each registered tool.
- Discuss why the fallback tool can give the wrong result.
