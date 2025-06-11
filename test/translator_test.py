"""
Tests the translator module for the assembler.
"""
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
def test_jump_lookup(mnemonic, expected_binary):
    assert jump_dict.get(mnemonic) == expected_binary
