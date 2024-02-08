## Canale Youtube di Edoardo Midali (codegrind.it)
## Raccolta di vari esempi per creare finestre e gestirne il layout management con il metodo GRID
##
## provo a fare il layout di VSCODE aggiungendo anche una MENUBAR

import tkinter as tk    #importo il odulo base di Tkinter
from tkinter import ttk #ttk è il sub-modulo per la grafica più moderna

#--> FINESTRA PRINCIPALE
finestra = tk.Tk()
finestra.title('Esempio numero 003')
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

#definisco i widget
frame1 = tk.LabelFrame(finestra, text="Icone", borderwidth=2, height=200, width=200)
frame2 = tk.LabelFrame(finestra, text='File', borderwidth=2, height=200, width=200)
frame3 = tk.LabelFrame(finestra, text='Testo', borderwidth=2, height=200, width=200)
frame4 = tk.LabelFrame(finestra, text='Output', borderwidth=2, height=200, width=200)

#bottone1 = tk.Button(text='Bottone1')
#bottone1.pack(frame1)

#assegno i frame alla griglia facendo columnspan o rowspan che simula l'unisci celle degli spreadsheet
frame1.grid(column=0, row=0, rowspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)
frame2.grid(column=1, row=0, rowspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)
frame3.grid(column=2, row=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)
frame4.grid(column=2, row=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

#creo widget e li assegno alla griglia

bottone1 = tk.Button(frame1, text='Bottone1')
bottone1.pack()
bottone2 = tk.Button(frame1, text='Bottone2')
bottone2.pack()
bottone3 = tk.Button(frame1, text='Bottone3')
bottone3.pack()
bottone4 = tk.Button(frame2, text='Bottone4')
bottone4.pack()
bottone5 = tk.Button(frame3, text='Bottone5')
bottone5.pack()
bottone6 = tk.Button(frame4, text='Bottone6')
bottone6.pack()

# window.mainloop() dice a Python di eseguire il ciclo degli eventi di Tkinter. 
finestra.mainloop()
