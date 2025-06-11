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

