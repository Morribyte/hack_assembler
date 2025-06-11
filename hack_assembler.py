"""
The hack assembler main file
"""
import argparse
from pathlib import Path

from src.parser import Parser
from src.translator import Translator

parser = Parser()

def get_file():
    """
    Prompts user for a file if not provided via command-line.
    """
    while True:
        file_path = input("Hack assembler > ").strip()
        if Path(file_path).exists():
            return file_path
        print("File not found. Try again.")


def get_parser():
    """
    Instantiates and returns an instance of the parser using the file_path.
    """

    print("Started parser.")
    return parser


def read_file(file_path):
    with open(file_path, "r") as file:
        lines: list[str] = [line.split("//")[0].rstrip() for line in file.readlines() if line.split("//")[0].strip()]
    print(lines)
    return lines


def run_parser(lines: list[str]):
    """
    Runs the parser
    """
    parser = get_parser()

    for index, line in enumerate(lines):
        if parser.is_a_command(line):
            lines[index] = parser.remove_symbol(line)
            print(f"[A command found]: Old value: {line} | New value: {lines[index]}")
        if parser.is_c_command(line):
            dest = parser.get_dest(line)
            comp = parser.get_comp(line)
            jump = parser.get_jump(line)
            print(f"[C command found]: Comp: {comp} | Dest: {dest} | Jump: {jump}")


def main():
    """
    Main function
    """
    parser = argparse.ArgumentParser(description="HACK Assembler")
    parser.add_argument("file", nargs="?", help="Assembles the given file into a .hack file.")

    args = parser.parse_args()
    file_path = args.file if args.file else get_file()
    print(f"Current file path: {file_path}")

    open_file = read_file(file_path)


if __name__ == "__main__":
    main()