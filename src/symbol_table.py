"""
src/symbol_table.py
Handles parsing symbols for the assembler.
"""

class SymbolTable:
    """
    Represents a symbol table object
    """
    symbol_table: dict = {
        # Pre-defined symbols
        "SP": "0", "LCL": "1", "ARG": "2", "THIS": "3", "THAT": "4",
        "R0": "0", "R1": "1", "R2": "2", "R3": "3", "R4": "4", "R5": "5",
        "R6": "6", "R7": "7", "R8": "8", "R9": "9", "R10": "10", "R11": "11",
        "R12": "12", "R13": "13", "R14": "14", "R15": "15", "SCREEN": "16384",
        "KBD": "24576"
    }
    next_available_ram = 16

    def __init__(self):
        pass

    def add_entry(self, symbol: str) -> str:
        """
        Adds a symbol entry to the table starting from RAM[16]
        """
        if symbol not in SymbolTable.symbol_table:
            SymbolTable.symbol_table[symbol] = str(SymbolTable.next_available_ram)
            SymbolTable.next_available_ram += 1
        return SymbolTable.symbol_table[symbol]

    def get_address(self, symbol: str) -> str:
        """
        Gets an address from the table.
        """
        return SymbolTable.symbol_table.get(symbol)