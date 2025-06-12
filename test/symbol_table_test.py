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