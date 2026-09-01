from typing import TypedDict
from langgraph.graph import END, StateGraph

class State(TypedDict): request: str; route: str; result: str
def classify(s): return {"route":"math" if any(c.isdigit() for c in s["request"]) else "explain"}
def math(s): return {"result":"Calculator route selected"}
def explain(s): return {"result":"Explanation route selected"}
g=StateGraph(State); g.add_node("classify",classify); g.add_node("math",math); g.add_node("explain",explain); g.set_entry_point("classify"); g.add_conditional_edges("classify",lambda s:s["route"],{"math":"math","explain":"explain"}); g.add_edge("math",END); g.add_edge("explain",END); app=g.compile()
if __name__ == "__main__": print(app.invoke({"request":input("Request: "),"route":"","result":""}))
