import ast
from pathlib import Path

def check(folder="sample_src"):
    errors=[]
    for path in Path(folder).rglob("*.py"):
        try: ast.parse(path.read_text(encoding="utf-8"))
        except SyntaxError as exc: errors.append(f"{path}:{exc.lineno}")
    return errors

if __name__ == "__main__":
    failures=check(); print("PASS" if not failures else "FAIL", failures); raise SystemExit(bool(failures))
