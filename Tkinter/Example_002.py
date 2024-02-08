## Canale Youtube di Edoardo Midali (codegrind.it)
## Raccolta di vari esempi per creare finestre, checkbutton, radiobutton

import tkinter as tk    #importo il odulo base di Tkinter
from tkinter import ttk #ttk è il sub-modulo per la grafica più moderna

# inserisco prima le funzioni che dovranno essere eseguite per alcuni eventi sui widget
def importa():
    print('Ho premuto importa')

def premo_check():
    print(valorecheck1.get())

def si_no():
    print(valorecheck2.get())
    # aggiungo la creazione dinamica di una label
    label = tk.Label(text=valorecheck2.get())
    label.pack()

#--> FINESTRA PRINCIPALE
# disegno una finestra
finestra = tk.Tk()

# do un titlo alla finestra
finestra.title('Example_002')

# imposto le dimensioni (attenzione alla sintassi)
finestra.geometry('800x800')

# carico un po' di icone da usare negli oggetti, non posso farlo prima di aver creato la finestra
ico_importa = tk.PhotoImage(file='./Tkinter/import.png')
ico_programma = tk.PhotoImage(file='./Tkinter/programma.png')

# assegno un'icona al programma
#finestra.iconbitmap('./Tkinter/program.ico') #non capisco perchè non funziona
finestra.iconphoto(True, ico_programma)

#--> WIDGETS
# creo widget di tipo CHECKBUTTON che esegue anche un comando
check = tk.Checkbutton(text="Python spacca a bestia!", font=('Helvetica'), command=importa)
check.pack()

# creo widget di tipo CHECKBUTTON e ne prendo il valore, prima devo definire una variabile
valorecheck1 = tk.BooleanVar()
check1 = tk.Checkbutton(text="Premi", font=('Helvetica'), command=premo_check, variable=valorecheck1)
check1.pack()

# creo widget di tipo CHECKBUTTON e specifico che deve avere, come valori, 'si' e 'no'
valorecheck2 = tk.StringVar()
check2 = tk.Checkbutton(text="Premi", font=('Helvetica'), command=si_no, variable=valorecheck2, onvalue='si', offvalue='no')
check2.pack()

# creo un widget di tipo RADIOBUTTON, tutti i widget della medesima domanda hanno stessa variabile perchè 
# devono essere alternativi tra di loro
domanda = tk.Label(text='Sei Maschio o Femmina?')
domanda.pack()

radiovar = tk.StringVar()
radio1 = tk.Radiobutton(text='Maschio', value='m', variable=radiovar)
radio2 = tk.Radiobutton(text='Femmina', value='f', variable=radiovar)
radio1.pack()
radio2.pack()

# Metto un bottone che chiede conferma della scelta e stampa il valore della variabile del radiobutton
bottone_ok = tk.Button(text='Confermi la scelta?', command=lambda:print(radiovar.get()))
bottone_ok.pack()

# Creo dinamicamente dei widget di tipo RadioButton in base ai valori di una tupla di tuple
taglia_selezionata = tk.StringVar()
taglie = (
    ('Small', 'S'),
    ('Medium', 'M'),
    ('Large', 'L'),
    ('Extra Large', 'XL')
)

for taglia in taglie:
    r = tk.Radiobutton(finestra, text=taglia[0], value=taglia[1], variable=taglia_selezionata)
    r.pack(padx=5, pady=5)

bottone_taglia = tk.Button(text='Confermi la scelta della taglia?', command=lambda:print(taglia_selezionata.get()))
bottone_taglia.pack()

# creo widget di tipo BUTTON con qualche proprietà (molto simili alle label) e un comando in linea (lambda)
bottone_quit = tk.Button(text='Esci', bg='red', width=10, height=5, borderwidth=3, command=lambda: finestra.quit())
bottone_quit.pack()

# window.mainloop() dice a Python di eseguire il ciclo degli eventi di Tkinter. 
finestra.mainloop()
