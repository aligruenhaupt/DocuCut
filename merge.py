import os
import sys
import PyPDF2


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