"""
Handles the tests for the parser
"""
from src.parser import Parser

import pytest

@pytest.fixture
def setup_resources():
    """
    Sets up the parser object and yields it
    """
    parser = Parser()

    yield {
        "parser": parser,
    }


def test_creation(setup_resources):
    """
    Test object creation for the parser
    """
    parser = setup_resources["parser"]
    assert parser is not None


def test_a_command(setup_resources):
    """
    Test that the parser recognizes when something is an A-type command.
    """
    parser = setup_resources["parser"]
    assert parser.is_a_command("@100")


def test_not_a_command(setup_resources):
    """
    Test that the parser successfully recognizes when something isn't an A command.
    """
    parser = setup_resources["parser"]
    assert parser.is_a_command("D=A") is False


def test_a_command_clean_symbol(setup_resources):
    """
    Test that the parser, when fed an A-command, will return just a string without the @ sign.
    """
    parser = setup_resources["parser"]
    precleaned_value: str = "@sum"
    print(precleaned_value)

    value = parser.remove_symbol(precleaned_value)
    print(value)
    assert value == "sum"


def test_is_c_command_equals_sign(setup_resources):
    """
    Test that we can tell if something's a C command by having an equals sign
    """
    parser = setup_resources["parser"]
    value = parser.is_c_command("M=M+1")
    assert value is True


def test_is_c_command_semicolon(setup_resources):
    """
    Test that we can tell if something's a C command by having a semicolon
    """
    parser = setup_resources["parser"]
    value = parser.is_a_command("0;JMP")
    assert value is True
