"""
src/translator.py
Handles translating the commands we retrieved from the parser into its constitutent binary code
"""

class Translator:
    """
    Represents a translator object
    """
    def __init__(self):
        pass

    def convert_jump(self, command: str) -> str:
        """
        Takes in a "C" command and returns a set of three bits.
        """
        return "111"