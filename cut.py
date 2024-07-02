import os
import sys
import PyPDF2

def cut_pdfs(output_file, pdf):
    pdf_writer = PyPDF2.PdfFileWriter()

    pdf_reader = PyPDF2.PdfReader(pdf.strip())


