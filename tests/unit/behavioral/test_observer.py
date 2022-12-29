"""
Tests for the Observer module.
"""

from unittest.mock import Mock
from behavioral import observer


def test_default_concrete_observer_state() -> None:
    concrete_observer = observer.ConcreteObserver(Mock())
    assert concrete_observer.state is None


def test_default_concrete_subject_state() -> None:
    subject = observer.ConcreteSubject()
    assert subject.state is None


def test_set_concrete_subject_state() -> None:
    subject = observer.ConcreteSubject()
    subject.set_state("test")
    assert subject.state == "test"


def test_observer_updates_state() -> None:
    subject = observer.ConcreteSubject()

    concrete_observer = observer.ConcreteObserver(subject)

    subject.attach(concrete_observer)

    subject.set_state("hello")

    assert concrete_observer.state == "hello"


def test_detach_observer() -> None:
    subject = observer.ConcreteSubject()
    concrete_observer = observer.ConcreteObserver(subject)

    subject.attach(concrete_observer)
    subject.detach(concrete_observer)
    subject.set_state("hello")

    assert concrete_observer.state is None


def test_bad_detach_is_ignore() -> None:
    subject = observer.ConcreteSubject()
    concrete_observer = observer.ConcreteObserver(subject)

    subject.detach(concrete_observer)


def test_notify_empty_no_error() -> None:
    subject = observer.ConcreteSubject()
    subject.notify()
