"""
Handles the tests for the parser
"""
from src.parser import Parser

import pytest

@pytest.fixture
def setup_resources():
    """
    Sets up the parser object and yields it
    """
    input_file = r"F:\Programming\Hack and ASM Projects\Assembler\temp\Add.asm"
    parser = Parser()

    yield {
        "parser": parser,
    }


def test_creation(setup_resources):
    """
    Test object creation for the parser
    """
    parser = setup_resources["parser"]
    assert parser is not None


def test_advance(setup_resources):
    """
    Test that parser.advance adds increments the line by 1.
    """
    parser = setup_resources["parser"]
    print(f"Current line: {parser.current_line}")
    parser.advance()
    print(f"Current line: {parser.current_line}")
    assert parser.current_line == 1


def test_a_command(setup_resources):
    """
    Test that the parser recognizes when something is an A-type command.
    """
    parser = setup_resources["parser"]
    assert parser.is_a_command("@100")


def test_not_a_command(setup_resources):
    """
    Test that the parser successfully recognizes when something isn't an A command.
    """
    parser = setup_resources["parser"]
    assert parser.is_a_command("D=A") is False


def test_a_command_clean_symbol(setup_resources):
    """
    Test that the parser, when fed an A-command, will return just a string without the @ sign.
    """
    parser = setup_resources["parser"]
    precleaned_value: str = "@sum"
    print(precleaned_value)

    value = parser.remove_symbol(precleaned_value)
    print(value)
    assert value == "sum"


def test_is_c_command_equals_sign(setup_resources):
    """
    Test that we can tell if something's a C command by having an equal sign
    """
    parser = setup_resources["parser"]
    assert parser.is_c_command("M=M+1") is True


def test_is_c_command_semicolon(setup_resources):
    """
    Test that we can tell if something's a C command by having a semicolon
    """
    parser = setup_resources["parser"]
    assert parser.is_c_command("0;JMP") is True


def test_is_c_command_both(setup_resources):
    """
    Test that having both "=" and ";", even if it doesn't happen in practice, still returns true.
    """
    parser = setup_resources["parser"]
    assert parser.is_c_command("M=M+1;JMP") is True


def test_a_command_inside_c_command(setup_resources):
    """
    Test that passing an "A" command will cause is_c_command to fail and vice versa
    """
    parser = setup_resources["parser"]
    assert parser.is_c_command("@100") is False
    assert parser.is_a_command("M=M+1") is False


def test_dest(setup_resources):
    """
    Test that we can pull the "dest" string from a "C" command
    """
    parser = setup_resources["parser"]
    value = parser.get_dest("M=M+1")
    print(value)
    assert value == "M"


def test_dest_no_equals(setup_resources):
    """
    Test that when there's no destination, we retrieve an empty string.
    """
    parser = setup_resources["parser"]
    value = parser.get_dest("0;JMP")
    print(value)
    assert value == "null"


def test_comp(setup_resources):
    """
    Test that we're able to grab the computation if it's present.
    """
    parser = setup_resources["parser"]
    value = parser.get_comp("M=M+1")
    print(value)
    assert value == "M+1"


def test_comp_no_equals(setup_resources):
    """
    Test that we're able to grab the computation even without an equals sign (e.g., for a jump)
    """
    parser = setup_resources["parser"]
    value = parser.get_comp("D;JMP")
    print(value)
    assert value == "D"


def test_comp_both_equals_semicolon(setup_resources):
    """
    Test that we're able to grab the computation even if we have both (even if it doesn't happen in practice)
    """
    parser = setup_resources["parser"]
    value = parser.get_comp("M=M+1;JMP")
    print(value)
    assert value == "M+1"


def test_get_jump(setup_resources):
    """
    Test that we're able to retrieve the jump portion of a "C" command
    """
    parser = setup_resources["parser"]
    value = parser.get_jump("D;JMP")
    print(value)
    assert value == "JMP"


def test_get_jump_no_semicolon(setup_resources):
    """
    Test that we retrieve an empty string when there's no jump command (e.g., there's no ";")
    """
    parser = setup_resources["parser"]
    value = parser.get_jump("M=M+1")
    print(value)
    assert value == "null"


@pytest.mark.parametrize("assembly_list, expected_is_a, expected_is_c, expected_dest, expected_jump, expected_comp",
[
    ("//Testing comment",False, False, "", "", ""),
    ("@100\n", True, False, "", "", ""),
    ("\n", False, False, "", "", ""),
    ("M=M+1", False, True, "M", "null", "M+1"),
    ("@sum", True, False, "", "", ""),
    ("MD=A", False, True, "MD", "null", "A"),
    ("D;JGT", False, True, "null", "JGT", "D"),
    ("0;JMP", False, True, "null", "JMP", "0"),
])
def test_full(setup_resources, assembly_list, expected_is_a, expected_is_c, expected_dest, expected_jump, expected_comp):
    """
    Test multiple parser methods to ensure correct output per command type.
    """
    parser = setup_resources["parser"]
    command = assembly_list.strip()  # Strip newlines & excess spaces before parsing

    print(f"Current item: {assembly_list} | expected_is_a: {expected_is_a} | expected_is_c: {expected_is_c} | expected_dest: {expected_dest} | expected jump: {expected_jump} | expected_comp: {expected_comp}")
    assert parser.is_a_command(command) == expected_is_a
    assert parser.is_c_command(command) == expected_is_c
    assert parser.get_dest(command) == expected_dest
    assert parser.get_jump(command) == expected_jump
    assert parser.get_comp(command) == expected_comp


def test_clean_line(setup_resources):
    """
    Test that a line cleans properly
    """
    line = '// Computes R0 = 2 + 3  (R0 refers to RAM[0])'
    parser = setup_resources["parser"]
    cleaned_line = parser.clean_line(line)
    print(cleaned_line)
