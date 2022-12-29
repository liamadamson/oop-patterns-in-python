"""
The Command design pattern.
"""

from typing import Protocol


class Command(Protocol):
    def execute(self) -> None:
        ...


class Button():
    """
    A Button that, when clicked, performed executes some Command.
    """

    def __init__(self, click_action: Command) -> None:
        self._click_action = click_action

    def click(self) -> None:
        self._click_action.execute()

    @property
    def click_action(self) -> Command:
        return self._click_action

    @click_action.setter
    def click_action(self, click_action: Command) -> None:
        self._click_action = click_action


class SayHello:
    def execute(self) -> None:
        print("Hello!")


class SayGoodbye:
    def execute(self) -> None:
        print("Bye!")
