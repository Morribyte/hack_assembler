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
    def get_dest(self, command: str) -> str:
        """
        takes a C command and retrieves the dest if it's there.
        command -> string - A line of assembly code.
        """
        if not self.is_c_command(command):
            return ""

        return command.split("=")[0] if "=" in command else "null"

    def get_comp(self, command: str) -> str:
        """
        takes a C command and retrieves the comp.
        command -> string - A line of assembly code.
        """
        if not self.is_c_command(command):
            return ""

        if "=" in command:
            command = command.split("=")[1]
        return command.split(";")[0]

    def get_jump(self, command: str) -> str:
        """
        takes a C command and retrieves the jump.
        command -> string - A line of assembly code.
        """
        if not self.is_c_command(command):
            return ""

        return command.split(";")[1] if ";" in command else "null"

    def remove_symbol(self, command: str) -> str:
        """
        takes an A-command that starts with an @, and returns the string without it.
        command -> string - A line of assembly code.
        """
        return command.replace("@", "")

    def extract_label(self, command: str) -> str:
        """Returns the label name by stripping parentheses."""
        return command.strip("()")

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

    def is_l_command(self, command: str) -> bool:
        """
        checks for an L command.
        command -> string - a line of assembly code
        """
        return command.startswith("(")

    def clean_line(self, command: str) -> str | None:
        """
        Cleans a line of whitespace and comments. Returns None if the line is only a comment.
        """
        command, _, _ = command.partition("//")
        cleaned = command.strip()
        return cleaned if cleaned else None  # Return None if nothing remains
