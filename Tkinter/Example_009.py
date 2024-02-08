## Canale Youtube di Edoardo Midali (codegrind.it)
## Creazione di TAB in finestra (notebook)

import tkinter as tk    #importo il odulo base di Tkinter
from tkinter import ttk #ttk è il sub-modulo per la grafica più moderna
from tkinter import scrolledtext

#--> FINESTRA PRINCIPALE
finestra = tk.Tk()
finestra.title('Esempio numero 009')
finestra.geometry('640x480')
ico_importa = tk.PhotoImage(file='./Tkinter/import.png')
ico_programma = tk.PhotoImage(file='./Tkinter/programma.png')
finestra.iconphoto(True, ico_programma)

# creo il raccoglitore di tab all'interno della finestra principale
notebook = ttk.Notebook(finestra)
notebook.pack(pady=10, fill='both', expand=True)

# creo e aggiungo i figli
frame1 = tk.Frame(notebook, width=400, height=200)
frame2 = tk.Frame(notebook, width=400, height=200)
frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

notebook.add(frame1, text='Tab1') #aggiungo il frame1 alla tab 1
notebook.add(frame2, text='Tab2') #aggiungo il frame2 alla tab 2

#aggiungo un po' di contenuti dentro alle tab
etichetta1 = tk.Label(frame1, text='Etichetta in Tab1', bg='red')
etichetta1.pack()

etichetta2 = tk.Label(frame2, text='Etichetta in Tab2', bg='green')
etichetta2.pack()
# window.mainloop() dice a Python di eseguire il ciclo degli eventi di Tkinter. 
finestra.mainloop()
