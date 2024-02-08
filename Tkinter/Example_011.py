## Canale Youtube di Edoardo Midali (codegrind.it)
## Creazione di un menu contestuale e messagebox

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

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
cont_menu.add_command(label="Info", 
                      command=lambda: messagebox.showinfo(title='Messaggio di informazione', message='Ecco l\'informazione')
                      )
cont_menu.add_command(label="Warning", 
                      command=lambda: messagebox.showwarning(title='Messaggio di warning', message='Ecco l\'informazione')
                      )
cont_menu.add_command(label="Errore", 
                      command=lambda: messagebox.showerror(title='Messaggio di errore', message='Ecco l\'informazione')
                      )
cont_menu.add_separator
cont_menu.add_command(label="Esci", command=(finestra.quit))

def show_message():
    risposta = messagebox.askyesno(title='Messaggio', message='Ti piace la pizza ?')
    # i più frequenti tipi di message box possono essere
    #askyesno
    #askyesnocancel
    #askokcancel
    #askretrycancel

    if risposta:
        print('Anche a me piace')
    else:
        print('Peccato, dovrebbe!')

mostra_messaggio = Button(text='Mostra messaggio', command=show_message).pack()

# creo la funzione che lo fa apparire a schermo
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
