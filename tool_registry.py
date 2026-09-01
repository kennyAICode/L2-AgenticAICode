from collections.abc import Callable


class ToolRegistry:
    def __init__(self):
        self._tools: dict[str, Callable[[str], str]] = {}

    def register(self, name: str, function: Callable[[str], str]) -> None:
        self._tools[name] = function

    def execute(self, name: str, argument: str) -> str:
        if name not in self._tools:
            raise KeyError(f"Unknown tool: {name}")
        return self._tools[name](argument)

    def names(self) -> list[str]:
        return list(self._tools)


def uppercase(text: str) -> str:
    return text.upper()


def word_count(text: str) -> str:
    return str(len(text.split()))


if __name__ == "__main__":
    registry = ToolRegistry()
    registry.register("uppercase", uppercase)
    registry.register("word_count", word_count)
    print("Tools:", registry.names())
    print(registry.execute("word_count", "Agents use tools to take action"))
