from dataclasses import dataclass, field

@dataclass
class State: goal: str; plan: list[str]=field(default_factory=list); output: str=""; score: int=0
def plan(s): s.plan=["understand goal","perform task","review result"]
def act(s): s.output=f"Completed: {s.goal}"
def evaluate(s): s.score=1 if s.output else 0

if __name__ == "__main__":
    s=State(input("Goal: "))
    for step in (plan,act,evaluate): step(s); print(step.__name__, s)
