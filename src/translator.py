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
            "null": "000", "JGT": "001", "JEQ": "010", "JGE": "011",
            "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111",
        }
        self.dest: dict = {
            "null": "000", "M": "001", "D": "010", "MD": "011",
            "A": "100", "AM": "101", "AD": "110", "AMD": "111",
        }
        self.comp: dict = {
            # Comp is usually 6 bits, but since you can add the 7th bit and use 0 or 1, it makes sense to put them here

            # A-bit = 0
            "0": "0101010", "1": "0111111", "-1": "0111010",
            "D": "0001100", "A": "0110001", "!D": "0001101", "!A": "0110001",
            "-D": "0001111", "-A": "0110011", "D+1": "0011111", "A+1": "0110111",
            "D-1": "0001110", "A-1": "0110010", "D+A": "0000010", "D-A": "0010011",
            "A-D": "0000111", "D&A": "0000000", "D|A": "0010101",

            # A-bit = 1
            "M": "1111010", "!M": "1110001", "-M": "1110011", "M+1": "1110111",
            "M-1": "1110010", "D+M": "1000010", "D-M": "1010011", "D&M": "1000000", "D|M": "1010101",
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