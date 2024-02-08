## Canale Youtube di Edoardo Midali (codegrind.it)
## Scrollbar applicata a listbox, scrolltext

import tkinter as tk    #importo il odulo base di Tkinter
from tkinter import ttk #ttk è il sub-modulo per la grafica più moderna
from tkinter import scrolledtext

#--> FINESTRA PRINCIPALE
finestra = tk.Tk()
finestra.title('Esempio numero 008')
finestra.geometry('640x480')
ico_importa = tk.PhotoImage(file='./Tkinter/import.png')
ico_programma = tk.PhotoImage(file='./Tkinter/programma.png')
finestra.iconphoto(True, ico_programma)

finestra.columnconfigure(0, weight=1)
finestra.rowconfigure(0, weight=1)
finestra.rowconfigure(1, weight=1)

#--> WIDGET
# per l'esempio prima creo una listbox
linguaggi = ('Javascript', 'Java', 'C', 'C++', 'Ruby', 'FoxPro', 'Go', 'PHP', 'Python', 'Clipper', 'Visual Basic',
             'Javascript', 'Java', 'C', 'C++', 'Ruby', 'FoxPro', 'Go', 'PHP', 'Python', 'Clipper', 'Visual Basic',
             'Javascript', 'Java', 'C', 'C++', 'Ruby', 'FoxPro', 'Go', 'PHP', 'Python', 'Clipper', 'Visual Basic',
             'Javascript', 'Java', 'C', 'C++', 'Ruby', 'FoxPro', 'Go', 'PHP', 'Python', 'Clipper', 'Visual Basic',
             'Javascript', 'Java', 'C', 'C++', 'Ruby', 'FoxPro', 'Go', 'PHP', 'Python', 'Clipper', 'Visual Basic'
             )
linguaggio_selezionato = tk.StringVar(value=linguaggi)
listbox = tk.Listbox(finestra, listvariable=linguaggio_selezionato, height=6, selectmode='extended')
listbox.grid(column=0, row=0, sticky='nwes')

#creo la scrollbar
scrollbar=ttk.Scrollbar(finestra, orient='vertical', command=listbox.yview) #creata ed assegnata a listbox, vista verticale
scrollbar.grid(row=0, column=1, sticky='ns') #inserita in girglia alla colonna 1 ed espansa in tutta altezza

listbox['yscrollcommand'] = scrollbar.set #collegata la scrollbar a listbox

#creaiamo uno scrolledtext (ad es una casella per i log di elaborazione)
scrolledtxt = scrolledtext.ScrolledText(finestra, width=50, height=10)
scrolledtxt.grid(column=0, row=1)

# window.mainloop() dice a Python di eseguire il ciclo degli eventi di Tkinter. 
finestra.mainloop()
