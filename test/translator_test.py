"""
Tests the translator module for the assembler.
"""
from glob import translate

from src.symbol_table import SymbolTable
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
    "0": "0101010", "1": "0111111", "-1": "0111010",
    "D": "0001100", "A": "0110000", "!D": "0001101", "!A": "0110001",
    "-D": "0001111", "-A": "0110011", "D+1": "0011111", "A+1": "0110111",
    "D-1": "0001110", "A-1": "0110010", "D+A": "0000010", "D-A": "0010011",
    "A-D": "0000111", "D&A": "0000000", "D|A": "0010101",

    # A-bit = 1
    "M": "1110000", "!M": "1110001", "-M": "1110011", "M+1": "1110111",
    "M-1": "1110010", "D+M": "1000010", "D-M": "1010011", "M-D": "1000111", "D&M": "1000000", "D|M": "1010101",
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
    print(mnemonic + ":" + expected_binary)
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
    print(mnemonic + ":" + expected_binary)
    assert translator.convert_dest(mnemonic) == expected_binary


def test_convert_comp(setup_resources):
    """
    Test that we can convert our comp to bits
    """
    translator = setup_resources["translator"]
    assert translator.convert_comp("!D") == "0001101"


@pytest.mark.parametrize("mnemonic, expected_binary", comp_dict.items())
def test_comp_lookup(setup_resources, mnemonic, expected_binary):
    """
    Test the comp lookup through all values
    """
    translator = setup_resources["translator"]
    print(mnemonic + ":" + expected_binary)
    assert translator.convert_comp(mnemonic) == expected_binary

