import json
from pathlib import Path

def checkpoint(state): Path("state.json").write_text(json.dumps(state,indent=2),encoding="utf-8")
def run(action):
    state={"action":action,"status":"waiting_for_approval"}; checkpoint(state)
    approved=input("Approve? (yes/no): ").lower()=="yes"; state["status"]="executed" if approved else "rejected"; checkpoint(state); return state
if __name__ == "__main__": print(run(input("Proposed action: ")))
