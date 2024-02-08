## Canale Youtube di Edoardo Midali (codegrind.it)
## Raccolta di vari esempi per creare finestre e gestirne il layout management con il metodo GRID
##
## provo a fare il layout di VSCODE aggiungendo anche una MENUBAR

import tkinter as tk    #importo il odulo base di Tkinter
from tkinter import ttk #ttk è il sub-modulo per la grafica più moderna

#--> FINESTRA PRINCIPALE
finestra = tk.Tk()
finestra.title('Editor di codice')
finestra.geometry('1024x768')
ico_importa = tk.PhotoImage(file='./Tkinter/import.png')
ico_programma = tk.PhotoImage(file='./Tkinter/programma.png')
finestra.iconphoto(True, ico_programma)

#--> Definizione GRID
# definisco la griglia
finestra.columnconfigure(0, weight=1)
finestra.columnconfigure(1, weight=500) 
finestra.columnconfigure(2, weight=5000) 
finestra.rowconfigure(0, weight=3) 
finestra.rowconfigure(1, weight=1)

# definisco i widget
frame1 = tk.LabelFrame(finestra, text="Icone", borderwidth=2, height=200, width=200)
frame2 = tk.LabelFrame(finestra, text='File', borderwidth=2, height=200, width=200)
frame3 = tk.LabelFrame(finestra, text='Testo', borderwidth=2, height=200, width=200)
frame4 = tk.LabelFrame(finestra, text='Output', borderwidth=2, height=200, width=200)

# creo anche una menubar, dapprima creo il menù e lo assegno alla finestra principale
menubar = tk.Menu(finestra) # con il parametro tearoff=0 elimino la prima riga in alto
finestra.config(menu=menubar)
# poi creo le voce di menù
file_menu = tk.Menu(menubar, tearoff=0) # con il parametro tearoff=0 elimino la prima riga in alto
file_modifica = tk.Menu(menubar)
file_help = tk.Menu(menubar)

# assegno alle voci al menu
menubar.add_cascade(label='File', menu=file_menu)
menubar.add_cascade(label='Modifica', menu=file_modifica)
menubar.add_cascade(label='Help', menu=file_help)

# creo i comandi sotto alle voci di menu
file_menu.add_command(label='New')
file_menu.add_command(label='Open')

# decido di fare un sottomenu
file_altro_submenu = tk.Menu(file_menu, tearoff=0)
file_altro_submenu.add_command(label='Ciao')
file_altro_submenu.add_command(label='Salve')
file_menu.add_cascade(label='Altro', menu=file_altro_submenu)

#continuo ad aggiungere i comandi
file_menu.add_separator()
file_menu.add_command(label='Esci', command=finestra.quit)

# assegno i frame alla griglia facendo columnspan o rowspan che simula l'unisci celle degli spreadsheet
frame1.grid(column=0, row=0, rowspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)
frame2.grid(column=1, row=0, rowspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)
frame3.grid(column=2, row=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)
frame4.grid(column=2, row=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

# creo il raccoglitore di tab all'interno del frame 3
notebook = ttk.Notebook(frame3)
notebook.pack(pady=10, fill='both', expand=True)

frame31 = tk.Frame(notebook, width=400, height=200)
frame32 = tk.Frame(notebook, width=400, height=200)
frame31.pack(fill='both', expand=True)
frame32.pack(fill='both', expand=True)

notebook.add(frame31, text='Tab1') #aggiungo il frame1 alla tab 1
notebook.add(frame32, text='Tab2') #aggiungo il frame2 alla tab 2

# creo widget e li assegno alla griglia
bottone1 = tk.Button(frame1, text='Bottone1')
bottone1.pack()
bottone2 = tk.Button(frame1, text='Bottone2')
bottone2.pack()
bottone3 = tk.Button(frame1, text='Bottone3')
bottone3.pack()
bottone4 = tk.Button(frame2, text='Bottone4')
bottone4.pack()
bottone5 = tk.Button(frame31, text='Bottone5')
bottone5.pack()
bottone6 = tk.Button(frame4, text='Bottone6')
bottone6.pack()
etichetta1 = tk.Label(frame32, text='ETICHETTA DI QUESTO FRAME', bg='green')
etichetta1.pack()

# window.mainloop() dice a Python di eseguire il ciclo degli eventi di Tkinter. 
finestra.mainloop()
