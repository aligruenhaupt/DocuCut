import tkinter as tk
from tkinter import filedialog

# Create the main window
root = tk.Tk()

# Create an entry widget
ent1 = tk.Entry(root, font=40)
ent1.grid(row=2, column=2)

# Define the browse function
def browsefunc(entry):
    filename = filedialog.askopenfilename(filetypes=(("pdf files", "*.pdf"), ("All files", "*.*")))
    entry.insert(tk.END, filename)

# Create a button that calls the browse function with the entry widget as argument
b1 = tk.Button(root, text="Browse...", font=40, command=lambda: browsefunc(ent1))  # Correct lambda usage
b1.grid(row=2, column=4)

# Run the application
root.mainloop()
