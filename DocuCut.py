import os
import sys
import PyPDF2
import cut


def get_terminal_size():

    try:
        size = os.get_terminal_size()
        return size
    except OSError:
        return os.terminal_size((80, 24))


def design_terminal():
    columns = get_terminal_size().columns - 1
    lines = get_terminal_size().lines - 1
    terminal_output = [[" " for _ in range(columns)] for _ in range(lines)]

    for i in range(lines):
        terminal_output[i][0] = "|"
        terminal_output[i][-1] = "|"

    for i in range(columns):
        terminal_output[0][i] = "_"
        terminal_output[-1][i] = "_"

    return terminal_output


def print_terminal(terminal_output):
    for i in range(get_terminal_size().lines - 1):
        for j in range(get_terminal_size().columns - 1):
            print(terminal_output[i][j], end="")
        print()


def add_line(terminal_output, line, text):
    char_text = list(text)

    for i in range(len(char_text)):
        terminal_output[line][2+i] = char_text[i]


def print_main_menu(terminal):
    add_line(terminal, 1, "DocuCut V0.1")
    add_line(terminal, 2, "made by Ali Yesilbas")
    add_line(terminal, 3, "h for help, q for quit")
    add_line(terminal, 4, "")
    add_line(terminal, 5, "")
    add_line(terminal, 6, "1: Merge PDFs")
    add_line(terminal, 7, "2: Cut PDFs")
    print_terminal(terminal)
    selected_mode = input("Please select a mode: ")
    return selected_mode


def print_merge_menu(terminal):
    terminal = design_terminal()
    add_line(terminal, 1, "DocuCut V0.1")
    add_line(terminal, 2, "merge PDFs")
    add_line(terminal, 3, "")
    add_line(terminal, 3, "Output File?")
    print_terminal(terminal)
    pdfs_path = input()


    print_main_menu(terminal)


terminall = design_terminal()

while True:
    mode = input("Please select a mode: ")








