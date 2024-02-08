## Canale Youtube di Edoardo Midali (codegrind.it)
## Raccolta di vari esempi per creare finestre e gestire ENTRY

import tkinter as tk    #importo il odulo base di Tkinter
from tkinter import ttk #ttk è il sub-modulo per la grafica più moderna

#--> FINESTRA PRINCIPALE
# disegno una finestra
finestra = tk.Tk()

# do un titlo alla finestra
finestra.title('Esempio numero 003')

# imposto le dimensioni (attenzione alla sintassi)
finestra.geometry('800x800')

# carico un po' di icone da usare negli oggetti, non posso farlo prima di aver creato la finestra
ico_importa = tk.PhotoImage(file='./Tkinter/import.png')
ico_programma = tk.PhotoImage(file='./Tkinter/programma.png')

# assegno un'icona al programma
#finestra.iconbitmap('./Tkinter/program.ico') #non capisco perchè non funziona
finestra.iconphoto(True, ico_programma)

#--> WIDGETS
# creo widget di tipo ENTRY per far inserire un valore all'utente


# creo widget di tipo BUTTON con qualche proprietà (molto simili alle label) e un comando in linea (lambda)
bottone_quit = tk.Button(text='Esci', bg='red', width=10, height=5, borderwidth=3, command=lambda: finestra.quit())
bottone_quit.pack()

# window.mainloop() dice a Python di eseguire il ciclo degli eventi di Tkinter. 
finestra.mainloop()
