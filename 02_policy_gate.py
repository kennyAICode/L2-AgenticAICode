from dataclasses import dataclass


@dataclass
class Action:
    name: str
    changes_data: bool
    external_recipient: bool


def requires_approval(action: Action) -> bool:
    return action.changes_data or action.external_recipient


if __name__ == "__main__":
    actions = [Action("search notes", False, False), Action("delete record", True, False),
               Action("send message", False, True)]
    for action in actions:
        print(action.name, "->", "HUMAN REVIEW" if requires_approval(action) else "AUTO-EXECUTE")

