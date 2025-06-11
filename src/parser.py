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

    def get_dest(self, command: str) -> str:
        """
        Takes a C command and retrieves the dest if it's there.
        """
        return command.split("=")[0] if "=" in command else ""


    def remove_symbol(self, command: str) -> str:
        """
        takes an A-command that starts with an @, and returns the string without it.
        command -> string - A line of assembly code.
        """
        return command.replace("@", "")

    def is_a_command(self, command: str) -> bool:
        """
        checks for an A command.
        command -> string - a line of assembly code.
        """
        return command.startswith("@")

    def is_c_command(self, command: str) -> bool:
        """
        checks for a C command.
        command -> string - a line of assembly code.
        """
        return "=" in command or ";" in command
