## Canale Youtube di Edoardo Midali (codegrind.it)
## Creazione di un menu contestuale

from tkinter import *
from tkinter import ttk

#--> FINESTRA PRINCIPALE
finestra = Tk()
finestra.title('Esempio numero 011')
finestra.geometry('640x480')
ico_importa = PhotoImage(file='./Tkinter/import.png')
ico_programma = PhotoImage(file='./Tkinter/programma.png')
finestra.iconphoto(True, ico_programma)

etichetta = Label(finestra, text='Ciao', bg='red')
etichetta.pack()

# definisco il menu contestuale
cont_menu = Menu(finestra, tearoff=0)
cont_menu.add_command(label="Taglia")
cont_menu.add_command(label="Copia")
cont_menu.add_command(label="Incolla")
cont_menu.add_separator
cont_menu.add_command(label="Esci", command=(finestra.quit))

# creao la funzione che lo fa apparire a schermo
def cont_menu_popup(event):
    try:
        cont_menu.tk_popup(event.x_root, event.y_root)
    finally:
        cont_menu.grab_release

# associo la funzione all'evento del tasto destro del mouse
etichetta.bind("<Button-3>", cont_menu_popup) #<Button-3> è il tasto destro del mouse

# prova per un ulteriore bind per uscire dalla maschera
def on_key_press(event):
    if event.keysym == "Escape":
        print('Hai premuto ESC')
        finestra.quit()

finestra.bind("<KeyPress>", on_key_press)

finestra.mainloop()
