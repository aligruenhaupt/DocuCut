import tkinter as tk
from tkinter import filedialog
from merge import merge_pdfs
import os


class GUI:

    def browsefunc(self, entry):
        filename = filedialog.askopenfilename(filetypes=(("pdf files", "*.pdf"), ("All files", "*.*")))
        entry.insert(tk.END, filename)

    def browse_output_path(self, entry_outputfile):
        directory_path = filedialog.askdirectory(initialdir="/home/ysl/")
        if directory_path:
            entry_outputfile.delete(0, tk.END)  # Clear any existing text in the entry
            entry_outputfile.insert(tk.END, directory_path)
        else:
            # Optionally show an error message or handle the case where no directory was selected
            print("Please select a valid directory.")

    def merge_files(self, entry_sourcefile_1, entry_sourcefile_2, entry_outputfile, entry_output_name, status_label):
        source_file_1 = entry_sourcefile_1.get()
        source_file_2 = entry_sourcefile_2.get()
        output_dir = entry_outputfile.get()
        output_name = entry_output_name.get()

        if not (source_file_1 and source_file_2 and output_dir and output_name):
            status_label.config(text="Please select source files and specify an output directory and file name.", fg="red")
            return

        output_file = os.path.join(output_dir, f"{output_name}.pdf")

        try:
            result_message = merge_pdfs(output_file, source_file_1, source_file_2)
            status_label.config(text=result_message, fg="green")
        except Exception as e:
            status_label.config(text=f"Error during merge: {str(e)}", fg="red")

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DocuCut")
        self.root.configure(bg="lavender")
        self.root.geometry("730x300")  # Adjusted window size for better visibility

        # Label and entry for Source File 1
        label_sourcefile_1 = tk.Label( self.root, bg="lavender", text="Source File 1:", font="Arial")
        label_sourcefile_1.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        entry_sourcefile_1 = tk.Entry(self.root, width=50, font="Arial")
        entry_sourcefile_1.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        button_browse_sf1 = tk.Button(self.root, text="Browse...", command=lambda: self.browsefunc(entry_sourcefile_1), font="Arial")
        button_browse_sf1.grid(row=0, column=2, padx=5, pady=5, sticky='w')

        # Label and entry for Source File 2
        label_sourcefile_2 = tk.Label(self.root, text="Source File 2:", font="Arial", bg="lavender")
        label_sourcefile_2.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        entry_sourcefile_2 = tk.Entry(self.root, width=50, font="Arial")
        entry_sourcefile_2.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        button_browse_sf2 = tk.Button(self.root, text="Browse...", command=lambda: self.browsefunc(entry_sourcefile_2), font="Arial")
        button_browse_sf2.grid(row=1, column=2, padx=5, pady=5, sticky='w')

        # Horizontal separator after Source File 2
        separator = tk.Frame(self.root, height=2, width=450, bg='black')
        separator.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='ew')

        # Label and entry for Output Directory
        label_outputfile = tk.Label(self.root, text="Output Directory:", font="Arial", bg="lavender")
        label_outputfile.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        entry_outputfile = tk.Entry(self.root, width=50, font="Arial")
        entry_outputfile.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        button_browse_output = tk.Button(self.root, text="Browse...", command=lambda: self.browse_output_path(entry_outputfile), font="Arial")
        button_browse_output.grid(row=3, column=2, padx=5, pady=5, sticky='w')

        # Label and entry for Output File Name
        label_outputname = tk.Label(self.root, text="Output File Name:", font="Arial", bg="lavender")
        label_outputname.grid(row=4, column=0, padx=10, pady=10, sticky='w')

        entry_output_name = tk.Entry(self.root, width=50, font="Arial")
        entry_output_name.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        # Merge button
        button_merge = tk.Button(self.root, font="Arial", text="Merge!", command=lambda: self.merge_files(entry_sourcefile_1, entry_sourcefile_2, entry_outputfile, entry_output_name, status_label))
        button_merge.grid(row=5, column=1, padx=5, pady=5, sticky='ew')

        # Status label for displaying merge status
        status_label = tk.Label(self.root, text="", fg="black", font="Arial")
        status_label.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

        self.root.mainloop()


if __name__ == "__main__":
    GUI()
