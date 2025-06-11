"""
Tests the translator module for the assembler.
"""
from src.translator import Translator

import pytest

@pytest.fixture
def setup_resources():
    """
    Creates the translator object and yields it
    """
    translator = Translator()

    yield {
        "translator": translator,
    }


def test_object(setup_resources):
    """
    Test that our translator object set up correctly.
    """
    translator = setup_resources["translator"]
    assert translator is not None
