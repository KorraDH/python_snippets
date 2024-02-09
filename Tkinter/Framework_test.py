import tkinter as tk
from tkinter import filedialog

def open_child_window():
    child_window = tk.Toplevel(root)
    child_window.title("Finestra Figlia")

    # Funzione chiamata quando viene selezionato un file
    def select_file():
        file_path = filedialog.askopenfilename(title="Seleziona un file", filetypes=[("All files", "*.*")])
        if file_path:
            label_file_path.config(text="Percorso del file: " + file_path)

    # Bottone per selezionare un file
    select_file_button = tk.Button(child_window, text="Seleziona un file", command=select_file)
    select_file_button.pack(pady=10)

    # Label per visualizzare il percorso del file
    label_file_path = tk.Label(child_window, text="Percorso del file: ")
    label_file_path.pack(pady=10)

# Finestra principale
root = tk.Tk()
root.title("Finestra Principale")

# Bottone per aprire la finestra figlia
open_child_button = tk.Button(root, text="Apri Finestra Figlia", command=open_child_window)
open_child_button.pack(pady=20)

root.mainloop()
