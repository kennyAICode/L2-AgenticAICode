from typing import TypedDict
from langgraph.graph import END, StateGraph

class State(TypedDict): topic: str; draft: str
def write(state): return {"draft": f"Beginner note about {state['topic']}"}
graph=StateGraph(State); graph.add_node("write",write); graph.set_entry_point("write"); graph.add_edge("write",END); app=graph.compile()
if __name__ == "__main__": print(app.invoke({"topic":input("Topic: "),"draft":""}))
