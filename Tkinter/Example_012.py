## Canale Youtube di Edoardo Midali (codegrind.it)
## Lavorare con i file

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

#--> FINESTRA PRINCIPALE
finestra = Tk()
finestra.title('Esempio numero 012')
finestra.geometry('640x480')
ico_importa = PhotoImage(file='./Tkinter/import.png')
ico_programma = PhotoImage(file='./Tkinter/programma.png')
finestra.iconphoto(True, ico_programma)

def apri_file():
    # definisco le estensioni possibili
    file_types = (
        ('File di testo', '*.txt *.csv'),
        ('Tutti i file', '*.*')
    )

    # chiedo di selezionare un file con le estensioni possibili
    filename = filedialog.askopenfilename(title='Seleziona un file', initialdir="/home", filetypes=file_types)
    #print(filename)

    # apro il file in lettura, metto i dati nella variabile data e li stampo
    f = open(filename, 'r')
    data = f.read()
    #print(type(data))
    print(data)

bottone = ttk.Button(finestra, text='Apri file', command=apri_file)
bottone.pack(expand=True)

def scrivi_file():
    f1 = filedialog.asksaveasfile(mode='w', title='Salva file', defaultextension='.txt')
    data2 = 'ajasljjd asj jasljdasljdasjda sdjlasj'
    f1.write(data2)
    f1.close()

bottone2 = Button(text='Scrivi sul file', command=scrivi_file)
bottone2.pack(expand=True)

# bind per uscire dalla maschera
def on_key_press(event):
    if event.keysym == "Escape":
        print('Hai premuto ESC')
        finestra.quit()

finestra.bind("<KeyPress>", on_key_press)

finestra.mainloop()
