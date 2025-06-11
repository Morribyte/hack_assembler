"""
src/translator.py
Handles translating the commands we retrieved from the parser into its constitutent binary code
"""

class Translator:
    """
    Represents a translator object
    """
    def __init__(self):
        self.jump: dict = {
            "null": "000",
            "JGT": "001",
            "JEQ": "010",
            "JGE": "011",
            "JLT": "100",
            "JNE": "101",
            "JLE": "110",
            "JMP": "111",
        }
        self.dest: dict = {
            "null": "000",
            "M": "001",
            "D": "010",
            "MD": "011",
            "A": "100",
            "AM": "101",
            "AD": "110",
            "AMD": "111",
        }

    def convert_jump(self, command: str) -> str:
        """
        Takes in a "C" command and returns a set of three bits.
        """
        return self.jump.get(command)

    def convert_dest(self, command: str) -> str:
        """
        Takes in a "C" command and returns a set of three bits.
        """
        return self.dest.get(command)