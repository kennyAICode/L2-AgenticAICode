from dataclasses import dataclass

@dataclass
class Task: text: str; worker: str=""; result: str=""
def supervisor(t): t.worker="calculator" if any(c.isdigit() for c in t.text) else "writer"
def calculator(t): t.result="Calculation worker received the task"
def writer(t): t.result="Writer produced a short explanation"
if __name__ == "__main__":
    t=Task(input("Task: ")); supervisor(t); {"calculator":calculator,"writer":writer}[t.worker](t); print(t)
