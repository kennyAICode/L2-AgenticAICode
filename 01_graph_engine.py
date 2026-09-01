from collections import defaultdict, deque
from collections.abc import Callable
from dataclasses import dataclass, field


@dataclass
class State:
    topic: str
    notes: list[str] = field(default_factory=list)
    draft: str = ""


class Graph:
    def __init__(self):
        self.nodes: dict[str, Callable[[State], None]] = {}
        self.edges: dict[str, list[str]] = defaultdict(list)

    def add_node(self, name: str, function: Callable[[State], None]) -> None:
        self.nodes[name] = function

    def add_edge(self, source: str, destination: str) -> None:
        self.edges[source].append(destination)

    def run(self, start: str, state: State) -> State:
        queue = deque([start])
        visited = set()
        while queue:
            node_name = queue.popleft()
            if node_name in visited:
                continue
            visited.add(node_name)
            print(f"Running node: {node_name}")
            self.nodes[node_name](state)
            queue.extend(self.edges[node_name])
        return state


def collect(state: State) -> None:
    state.notes.extend([f"Definition of {state.topic}", f"Example of {state.topic}"])


def draft(state: State) -> None:
    state.draft = " | ".join(state.notes)


if __name__ == "__main__":
    graph = Graph()
    graph.add_node("collect", collect)
    graph.add_node("draft", draft)
    graph.add_edge("collect", "draft")
    result = graph.run("collect", State(input("Topic: ")))
    print("Result:", result.draft)

