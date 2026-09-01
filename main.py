from dataclasses import dataclass

@dataclass
class Release: version: str; tests_passed: bool; approval: bool=False; environment: str="dev"
def promote(r):
    if not r.tests_passed: raise ValueError("Tests failed")
    if r.environment == "staging" and not r.approval: raise PermissionError("Production approval required")
    r.environment = {"dev":"staging", "staging":"production"}.get(r.environment, r.environment); return r

if __name__ == "__main__":
    item=Release("1.0.0", True); print(promote(item)); item.approval=True; print(promote(item))
