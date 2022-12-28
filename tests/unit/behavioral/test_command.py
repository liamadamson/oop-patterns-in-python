"""
Tests for the Command design pattern.
"""

import pytest
from unittest.mock import patch, Mock
from behavioral.command import SayHello, SayGoodbye, Button


@pytest.fixture(name="hello_button")
def fixture_hello_button() -> Button:
    hello_command = SayHello()
    return Button(hello_command)


@patch("builtins.print")
def test_initial_command(mock_print: Mock, hello_button: Button) -> None:
    hello_button.click()
    mock_print.assert_called_with("Hello!")


@patch("builtins.print")
def test_can_swap_command(mock_print: Mock, hello_button: Button) -> None:
    goodbye_command = SayGoodbye()
    hello_button.click_action = goodbye_command
    hello_button.click()
    mock_print.assert_called_with("Bye!")
