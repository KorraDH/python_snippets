## https://realpython.com/python-gui-tkinter/
## Raccolta di vari esempi per creare finestre, label e bottoni

import tkinter as tk    #importo il odulo base di Tkinter
from tkinter import ttk #ttk è il sub-modulo per la grafica più moderna

# inserisco prima le funzioni che dovranno essere eseguite per alcuni eventi sui widget
def importa():
    print('Ho premuto il bottone importa')

#--> FINESTRA PRINCIPALE
# disegno una finestra
finestra = tk.Tk()

# do un titlo alla finestra
finestra.title('Example_001')

# imposto le dimensioni (attenzione alla sintassi)
finestra.geometry('800x800')

# carico un po' di icone da usare negli oggetti, non posso farlo prima di aver creato la finestra
ico_importa = tk.PhotoImage(file='./Tkinter/import.png')
ico_programma = tk.PhotoImage(file='./Tkinter/programma.png')

# assegno un'icona al programma
#finestra.iconbitmap('./Tkinter/program.ico') #non capisco perchè non funziona
finestra.iconphoto(True, ico_programma)

# altre proprietà varie
#finestra.resizable(False, False)
#finestra.minsize(200,200)
#finestra.maxsize(1000,1000)
#finestra.attributes('-topmost', 1) #sempre in primo piano
#finestra.lift() #fai apparire in alto nello stack
#finestra.lower() #fai apparire in fondo nello stack

#finestra.wait_visibility(finestra) #per far funzionare gli atributi sotto
#finestra.attributes('-alpha',0.5)

#--> WIDGETS
# creo widget di tipo label, apparirà sempre una finestra vuota
etichetta = tk.Label(text="Python spacca a bestia!")

# metto il widget all'interno della finestra con il metodo pack. 
# Esistono anche i metodi "grid" per dare coordinate al widget rispetto alla griglia creata 
# e "assign" per dare coordinate assolute
etichetta.pack()

# creo una label colorata
etichetta_colorata = tk.Label(
    text="Etichetta Colorata",
    foreground="red",  # Set the text color to white, abbreviabile in "fg"
    background="black"  # Set the background color to black, abbreviabile in "bg"
)
etichetta_colorata.pack()

# creo una label colorata e larghezza personalizzata
etichetta_colorata2 = tk.Label(
    text="Etichetta Colorata e dimensionata",
    foreground="yellow",  # Set the text color to white, abbreviabile in "fg"
    background="blue",  # Set the background color to black, abbreviabile in "bg"
    width=50
)
etichetta_colorata2.pack()

# creo una label un po' più grande con le proprietà padx e pady e cambio font
# il pad è lo spazio bianco tra la fine dell'elemento e la fine del contenuto
# il pad è lo spazio vuoto all'interno dell'elemento mentre i margine è lo spazio vuoto all'esterno
# il parametro justify entra in gioco unicamente quando ho almeno due righe
etichetta2 = tk.Label(text='Ciao! \nSono Korra', bg='yellow', padx=20, pady=20, font=('Helvetica', 16), justify='left')
etichetta2.pack()

# creo una terza label come sopra ma inserisco anche un'immagine; 
# se non specifico il parametro compound l'immagine sarà sopra al testo; 
# mentre con compound specifico dove dev'essere posizionata l'immagine (top, bottom, left, right)
etichetta3 = tk.Label(text='Ecco l\'icona\n del programma', bg='grey', padx=20, pady=10, font=('Helvetica', 16)
                      , image=ico_programma, compound='top') 
etichetta3.pack()

# creo widget di tipo button con qualche proprietà (molto simili alle label) e un comando di callback
bottone = tk.Button(text='Prova bottone', bg='orange', width=10, height=5, borderwidth=3, command=importa)
bottone.pack()

# creo widget di tipo button con lo stato disabilitato
bottone_test = ttk.Button(text='BOTTONE')
bottone_test['state'] = 'disabled'
bottone_test.pack()

# creo widget di tipo button con immagini
bottone_imp = tk.Button(text='Importa dati', image=ico_importa, borderwidth=3, compound=('top'), command=importa)
bottone_imp.pack(ipadx=20, ipady=20) #nel metodo pack posso specificare il pad


# creo widget di tipo button con qualche proprietà (molto simili alle label) e un comando in linea (lambda)
bottone_quit = tk.Button(text='Esci', bg='red', width=10, height=5, borderwidth=3, command=lambda: finestra.quit())
bottone_quit.pack()

# window.mainloop() dice a Python di eseguire il ciclo degli eventi di Tkinter. 
# Questo metodo ascolta eventi, come clic su pulsanti o pressioni di tasti, 
# e blocca l'esecuzione di qualsiasi codice successivo finché non chiudi la finestra in cui hai chiamato il metodo.
#
# Se non includi window.mainloop() alla fine di un programma in un file Python,
# l'applicazione Tkinter non verrà mai eseguita e non verrà visualizzato nulla.
finestra.mainloop()

