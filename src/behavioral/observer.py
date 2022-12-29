"""
Observer design pattern.
"""

import abc
from typing import Set, Optional, Protocol


class Observer(Protocol):
    def update(self) -> None:
        ...


class Subject(abc.ABC):
    def __init__(self) -> None:
        self._observers: Set[Observer] = set()

    def attach(self, observer: Observer) -> None:
        self._observers.add(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update()


class ConcreteSubject(Subject):
    def __init__(self) -> None:
        super().__init__()
        self._state: Optional[str] = None

    @property
    def state(self) -> Optional[str]:
        return self._state

    def set_state(self, state: str) -> None:
        self._state = state
        self.notify()


class ConcreteObserver:
    def __init__(self, subject: ConcreteSubject) -> None:
        self._subject = subject
        self._state: Optional[str] = None

    @property
    def state(self) -> Optional[str]:
        return self._state

    def update(self) -> None:
        self._state = self._subject.state
