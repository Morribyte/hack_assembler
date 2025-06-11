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

dest_dict: dict = {
            "null": "000",
            "M": "001",
            "D": "010",
            "MD": "011",
            "A": "100",
            "AM": "101",
            "AD": "110",
            "AMD": "111",
        }
comp_dict: dict = {
    "0": "101010",
    "1": "111111",
    "-1": "111010",
    "D": "001100",
    "A": "110001",
    "!D": "001101",
    "!A": "110001",
    "-D": "001111",
    "-A": "110011",
    "D+1": "011111",
    "A+1": "110111",
    "D-1": "001110",
    "A-1": "110010",
    "D+A": "000010",
    "D-A": "010011",
    "A-D": "000111",
    "D&A": "000000",
    "D|A": "010101",
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
    """
    Test the jump lookup through all values
    """
    translator = setup_resources["translator"]
    assert translator.convert_jump(mnemonic) == expected_binary


def test_convert_dest(setup_resources):
    """
    Test that our destination field converts properly
    """
    translator = setup_resources["translator"]
    assert translator.convert_dest("M") == "001"


@pytest.mark.parametrize("mnemonic, expected_binary", dest_dict.items())
def test_dest_lookup(setup_resources, mnemonic, expected_binary):
    """
    Test the dest lookup through all values
    """
    translator = setup_resources["translator"]
    assert translator.convert_dest(mnemonic) == expected_binary


def test_convert_comp(setup_resources):
    """
    Test that we can convert our comp to bits
    """
    translator = setup_resources["translator"]
    assert translator.convert_comp("!D") == "001101"


@pytest.mark.parametrize("mnemonic, expected_binary", comp_dict.items())
def test_comp_lookup(setup_resources, mnemonic, expected_binary):
    """
    Test the comp lookup through all values
    """
    translator = setup_resources["translator"]
    assert translator.convert_comp(mnemonic) == expected_binary
