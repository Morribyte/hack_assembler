"""
The hack assembler main file
"""
import argparse
from pathlib import Path

from src.parser import Parser
from src.translator import Translator
from src.symbol_table import SymbolTable

parser = Parser()
translator = Translator()
symbol_table = SymbolTable()

def get_file():
    """
    Prompts user for a file if not provided via command-line.
    """
    while True:
        file_path = input("Hack assembler > ").strip()
        if Path(file_path).exists():
            return file_path
        print("File not found. Try again.")


def read_file(file_path):
    with open(file_path, "r") as file:
        lines: list[str] = [line.split("//")[0].rstrip() for line in file.readlines() if line.split("//")[0].strip()]
    lines = [line.strip() for line in lines]
    print(lines)
    return lines


def run_first_loop(lines: list[str]):
    """
    This loop runs through everything, grabbing symbols and appending them to the symbol table.
    Specifically, it looks for labels. We use the program counter to keep track of the implicit line for each insturction.
    When we encounter a label, we take the address of the next program counter and stick it into the symbol table.
    When the second pass happens, the assembler will know when it encounters (LOOP) to replace it with the instruction

    Labels: Starts with a left parenthesis "(". When enclosed with a ")" and there is a word inside it, it is a label.
        When this happens, the symbol table converts it to the number of the next machine instruction.
        For example, if one line is (LOOP) and the next is @R2, then the loop should be replaced wit
    """
    print("------------STARTING FIRST PASS------------\n")

    print(f"Program counter: {SymbolTable.program_counter}")
    print("Checking for L Command...")

    for index, line in enumerate(lines):
        if parser.is_l_command(line):
            print("L command found.")
            extracted_label: str = parser.extract_label(line)
            print(f"Extracted label: {extracted_label}")
            print(f"Address for symbol table: {SymbolTable.program_counter}")
            symbol_table.add_entry(extracted_label, SymbolTable.program_counter)
            print(lines[index])
            print(f"New lines: {lines[index]}")
            continue
        symbol_table.increment_pc()
        print(f"Current PC: {SymbolTable.program_counter}")
    # print("\n-----------FINAL LIST------------")
    # print(f"{lines}\n")
    print("-----------SYMBOL TABLE------------")
    print(f"{SymbolTable.symbol_table}\n")
    lines = [line for line in lines if not line.startswith("(")]
    return lines

def run_second_loop(lines: list[str]):
    """
    Finally translates everything to binary code.
    """
    print("------------STARTING SECOND PASS------------")
    for index, line in enumerate(lines):
        print(f"Current index: {index}")

        if parser.is_a_command(line):
            lines[index] = parser.remove_symbol(line)
            print(f"[A command found]: Old value: {line} | New value: {lines[index]}")
            if lines[index].isdigit():
                lines[index] = str(bin(int(lines[index]))[2:].zfill(16))
            else:
                address = symbol_table.get_address(lines[index])
                print(f"Address: {address}")
                if address is None and not lines[index].isdigit():
                    print(f"Address {address} found -- adding to list")
                    address = symbol_table.add_entry(lines[index])
                lines[index] = str(bin(int(address))[2:].zfill(16))

            print(f"{lines[index]} added to list\n")
        if parser.is_c_command(line):
            dest = parser.get_dest(line)
            comp = parser.get_comp(line)
            jump = parser.get_jump(line)
            print(f"[C command found]: Comp: {comp} | Dest: {dest} | Jump: {jump}")

            convert_dest = translator.convert_dest(dest)
            convert_comp = translator.convert_comp(comp)
            convert_jump = translator.convert_jump(jump)

            print(f"[Converted C]: Comp: {convert_comp} | Dest: {convert_dest} | Jump: {convert_jump}")

            # Use hard-coded value 111 since the first three bits in a c-instruction will always be 1.
            translated_instruction = "111" + convert_comp + convert_dest + convert_jump
            print(f"Translated instruction {translated_instruction} added to list\n")

            lines[index] = translated_instruction

    return lines


def write_to_file(file_name: str, translated_file: list[str]):
    """
    Writes a translated list to a file, line by line.
    """
    with open(f"output/{file_name}.hack", "w") as file:
        file.writelines(f"{line}\n" for line in translated_file)


def main():
    """
    Main function
    """
    parse = argparse.ArgumentParser(description="HACK Assembler")
    parse.add_argument("file", nargs="?", help="Assembles the given file into a .hack file.")

    args = parse.parse_args()
    file_path: Path = Path(args.file if args.file else get_file())
    file_name: str = file_path.stem

    print(f"Current file path: {file_path}")
    print(f"Current file name: {file_path.stem}")


    open_file = read_file(file_path)

    print(f"Translating file...\n")

    first_loop = run_first_loop(open_file)
    translated_file = run_second_loop(first_loop)
    print(f"Stripping translated file of any whitespace...\n")
    translated_file = [line.strip() for line in translated_file]
    print(f"Translation complete!\n")

    write_to_file(file_name, translated_file)

if __name__ == "__main__":
    main()
