from typing import Annotated, TypedDict
from operator import add
from langgraph.graph import END, StateGraph

class State(TypedDict): messages: Annotated[list[str], add]
def first(state): return {"messages":["planner created a task"]}
def second(state): return {"messages":["worker completed the task"]}
g=StateGraph(State); g.add_node("plan",first); g.add_node("work",second); g.set_entry_point("plan"); g.add_edge("plan","work"); g.add_edge("work",END); app=g.compile()
if __name__ == "__main__": print(app.invoke({"messages":[]}))
