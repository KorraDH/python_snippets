## Canale Youtube di Edoardo Midali (codegrind.it)
## Creazione di TREEVIEW in formati di "tabulardata" (tabella)

import tkinter as tk    #importo il odulo base di Tkinter
from tkinter import ttk #ttk è il sub-modulo per la grafica più moderna
from tkinter import scrolledtext

#--> FINESTRA PRINCIPALE
finestra = tk.Tk()
finestra.title('Esempio numero 010')
finestra.geometry('640x480')
ico_importa = tk.PhotoImage(file='./Tkinter/import.png')
ico_programma = tk.PhotoImage(file='./Tkinter/programma.png')
finestra.iconphoto(True, ico_programma)

# creo la tabella
colonne = ('nome', 'cognome', 'email')
tabella = ttk.Treeview(finestra, columns=colonne, show='headings')

# Definisco per bene i nomi delle colonne (estetica)
tabella.heading('nome', text='Nome Utente')
tabella.heading('cognome', text='Cognome Utente')
tabella.heading('email', text='E-mail')

# popolo le righe con un ciclo for
righe = []
for n in range(1,50):
    righe.append((f'Nome {n}', f'Cognome {n}', f'email{n}'))

# riempio la tabella con le righe
for riga in righe:
    tabella.insert('', 'end', values=riga)

# metto la tabella nella finestra
tabella.grid(row=0, column=0, sticky='nwse')

#aggiungo la scrollbar
scrollbar=ttk.Scrollbar(finestra, orient='vertical', command=tabella.yview)
scrollbar.grid(row=0, column=1, sticky='ns')
tabella.configure(yscrollcommand=scrollbar.set)

# window.mainloop() dice a Python di eseguire il ciclo degli eventi di Tkinter. 
finestra.mainloop()
