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
        self.comp: dict = {
            "0": "101010",
            "1": "111111",
            "-1": "111010",
            "D": "001100",
            "A": "110001",
            "!D": "001101",
            "!A": "110001",
            "-D": "001111",
            "-A": "110011",
            "D+1": "011111",
            "A+1": "110111",
            "D-1": "001110",
            "A-1": "110010",
            "D+A": "000010",
            "D-A": "010011",
            "A-D": "000111",
            "D&A": "000000",
            "D|A": "010101",
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

    def convert_comp(self, command: str) -> str:
        """
        Takes in a "C" command and returns a set of six bits.
        """
        return self.comp.get(command)