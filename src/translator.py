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

    def convert_jump(self, command: str) -> str:
        """
        Takes in a "C" command and returns a set of three bits.
        """
        return self.jump.get(command)