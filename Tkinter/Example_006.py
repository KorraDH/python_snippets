## Canale Youtube di Edoardo Midali (codegrind.it)
## Raccolta di vari esempi per creare finestre e gestirne il layout management con il metodo GRID

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
finestra.columnconfigure(1, weight=1) 

#definisco i widget
frame1 = tk.Frame(finestra, bg='red', height=200, width=200)
frame2 = tk.Frame(finestra, bg='green', height=200, width=200)
frame3 = tk.Frame(finestra, bg='purple', height=200, width=200)
frame4 = tk.Frame(finestra, bg='yellow', height=200, width=200)

'''
#assegno i widget alla griglia tutti uguali
frame1.grid(column=0, row=0)
frame2.grid(column=1, row=0)
frame3.grid(column=0, row=1)
frame4.grid(column=1, row=1)
'''

#assegno i widget alla griglia facendo columnspan o rowspan che simula l'unisci celle degli spreadsheet
frame1.grid(column=0, row=0, rowspan=2)
frame2.grid(column=1, row=0)
frame3.grid(column=0, row=2, columnspan=2)
frame4.grid(column=1, row=1)

# window.mainloop() dice a Python di eseguire il ciclo degli eventi di Tkinter. 
finestra.mainloop()
