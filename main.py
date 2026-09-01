from typing import TypedDict
from langgraph.graph import END, StateGraph

class State(TypedDict): goal:str; plan:str; work:str; review:str
def planner(s): return {"plan":f"Plan for {s['goal']}"}
def worker(s): return {"work":f"Completed {s['plan']}"}
def reviewer(s): return {"review":"approved" if s["work"] else "rejected"}
g=StateGraph(State); [g.add_node(n,f) for n,f in [("planner",planner),("worker",worker),("reviewer",reviewer)]]; g.set_entry_point("planner"); g.add_edge("planner","worker"); g.add_edge("worker","reviewer"); g.add_edge("reviewer",END); app=g.compile()
if __name__ == "__main__": print(app.invoke({"goal":input("Goal: "),"plan":"","work":"","review":""}))
