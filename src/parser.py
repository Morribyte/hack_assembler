"""
src/parser.py
Handles turning each line of assembler code into its constituent parts.
C-commands -> Turns into the dest, comp, and jump parts.
A-commands -> ignores @ symbols
Labels -> Ignores (for now)
"""

class Parser:
    """
    Represents an assembler parser object
    """
    def __init__(self):
        pass

    def is_a_command(self, command: str) -> bool:
        """
        Checks which type of command a line of code is.
        command -> string. A line of assembly code.
        """
        return command.startswith("@")