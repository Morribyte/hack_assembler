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


def test_first_line(setup_resources):
    """
    Test that the parser can see a given argument.
    """
    parser = setup_resources["parser"]
    value = parser.check_command()
    assert value == "M=M+1"