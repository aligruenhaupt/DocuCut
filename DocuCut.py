import os
import sys
import PyPDF2

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
    add_line(terminal, 2, "Merge PDFs")
    add_line(terminal, 3, "")
    add_line(terminal, 4, "Enter output file name:")
    print_terminal(terminal)
    output_file = input()
    add_line(terminal, 5, "Enter paths of PDFs to merge (comma separated):")
    print_terminal(terminal)
    pdfs = input().split(',')
    merge_pdfs(output_file, pdfs)

def merge_pdfs(output_file, pdfs):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf_path in pdfs:
        try:
            pdf_reader = PyPDF2.PdfReader(pdf_path.strip())
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)
        except FileNotFoundError:
            print(f"File {pdf_path} not found. Skipping.")
        except PyPDF2.errors.PdfReadError:
            print(f"Error reading {pdf_path}. Skipping.")

    with open(output_file, 'wb') as out:
        pdf_writer.write(out)
    print(f"Merged PDF saved as {output_file}")

def main():
    while True:
        terminal_output = design_terminal()
        selected_mode = print_main_menu(terminal_output)

        if selected_mode == '1':
            print_merge_menu(terminal_output)
        elif selected_mode == '2':
            # Add your cut PDF functionality here
            pass
        elif selected_mode == 'h':
            print("Help: Use 1 to merge PDFs, 2 to cut PDFs, q to quit.")
        elif selected_mode == 'q':
            print("Quitting...")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
