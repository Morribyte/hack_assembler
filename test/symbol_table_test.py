"""
Testing for the symbol table
"""

from src.symbol_table import SymbolTable

import pytest

@pytest.fixture
def setup_resources():
    """
    Creates the SymbolTable object and returns it
    """
    symbol = SymbolTable()

    yield {
        "symbol": symbol,
    }


def create_object(setup_resources):
    """
    Tests that symbol tree isnt empty
    """
    symbol = setup_resources["symbol"]
    assert symbol is not None


def test_add_entry(setup_resources):
    """
    Tests that we can add an entry to the table
    """
    symbol = setup_resources["symbol"]
    symbol.add_entry("add")
    symbol.add_entry("sub")
    symbol.add_entry("div")
    assert SymbolTable.symbol_table.get("add") == "16"
    assert SymbolTable.symbol_table.get("sub") == "17"
    assert SymbolTable.symbol_table.get("div") == "18"


def test_get_address(setup_resources):
    """
    Tests that given a key, we retrieve the value.
    """
    symbol = setup_resources["symbol"]
    value = symbol.get_address("SCREEN")
    print(value)
    assert value == "16384"


def test_program_counter(setup_resources):
    """
    Test that the program counter increments properly when given an instruction
    """
    symbol = setup_resources["symbol"]
    assert SymbolTable.program_counter == 0

    symbol.increment_pc()
    assert SymbolTable.program_counter == 1


def test_automated_incrementing(setup_resources):
    """
    Test that our program counter increments properly to large numbers
    """
    symbol = setup_resources["symbol"]
    SymbolTable.program_counter = 0

    for _ in range (30000):
        symbol.increment_pc()
        if SymbolTable.program_counter % 1000 == 0:
            print(f"Program counter: {SymbolTable.program_counter}")
    assert SymbolTable.program_counter == 30000
