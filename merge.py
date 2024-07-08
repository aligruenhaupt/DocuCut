import PyPDF2

def merge_pdfs(output_file, source_file_1, source_file_2):
    pdf_writer = PyPDF2.PdfWriter()

    pdf_paths = [source_file_1, source_file_2]

    for pdf_path in pdf_paths:
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

    return f"Merged PDF saved as {output_file}"
