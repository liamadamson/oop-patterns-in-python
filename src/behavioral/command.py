"""
The Command design pattern.
"""


import abc


class Command(abc.ABC):
    @abc.abstractmethod
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


class SayHello(Command):
    def execute(self) -> None:
        print("Hello!")


class SayGoodbye(Command):
    def execute(self) -> None:
        print("Bye!")
