"""
src/parser.py
Handles turning each line of assembler code into its constituent parts.
C-commands -> Turns into the dest, comp, and jump parts.
A-commands -> ignores @ symbols
Labels -> Ignores (for now)
"""

from pathlib import Path

class Parser:
    """
    Represents an assembler parser object
    """
    def __init__(self, input_file: str | Path):
        self.input_file: Path = Path(input_file)
        self.current_line: int = 0
        with open(self.input_file, "r") as file:
            self.lines: list[str] = [line.strip() for line in file.readlines()]

    def advance(self):
        """
        Advances the self.current_line count by 1.
        """
        self.current_line = self.current_line + 1

    def get_dest(self, command: str) -> str:
        """
        takes a C command and retrieves the dest if it's there.
        command -> string - A line of assembly code.
        """
        return command.split("=")[0] if "=" in command else ""

    def get_comp(self, command: str) -> str:
        """
        takes a C command and retrieves the comp.
        command -> string - A line of assembly code.
        """
        if "=" in command:
            command = command.split("=")[1]
        return command.split(";")[0]

    def get_jump(self, command: str) -> str:
        """
        takes a C command and retrieves the jump.
        command -> string - A line of assembly code.
        """
        return command.split(";")[1] if ";" in command else ""

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
