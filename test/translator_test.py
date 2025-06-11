"""
Tests the translator module for the assembler.
"""
from glob import translate

from src.translator import Translator

import pytest

jump_dict: dict = {
            "null": "000",
            "JGT": "001",
            "JEQ": "010",
            "JGE": "011",
            "JLT": "100",
            "JNE": "101",
            "JLE": "110",
            "JMP": "111",
        }

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


def test_convert_jump(setup_resources):
    """
    Test that we can convert the jump command to bits
    """
    translator = setup_resources["translator"]
    value = translator.convert_jump("JMP")
    print(value)
    assert value == "111"


@pytest.mark.parametrize("mnemonic, expected_binary", jump_dict.items())
def test_jump_lookup(setup_resources, mnemonic, expected_binary):
    translator = setup_resources["translator"]
    assert translator.convert_jump(mnemonic) == expected_binary


def test_no_jump(setup_resources):
    """
    Test that we return a null when there's no jump command.
    """
    translator = setup_resources["translator"]
    value = translator.convert_jump("null")
    assert value == "000"
