## Canale Youtube di Edoardo Midali (codegrind.it)
## Raccolta di vari esempi per creare finestre e gestire ENTRY e COMBOBOX

import tkinter as tk    #importo il odulo base di Tkinter
from tkinter import ttk #ttk è il sub-modulo per la grafica più moderna
from calendar import month_name #serve per la combo dopo

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

def login():
    print(email_entry.get())
    print(passwrod_entry.get())

def sleeziona_mese(event):
    print(mese_selezionato.get())

#--> WIDGETS
# creo widget di tipo ENTRY per far inserire un valore all'utente
label_email = tk.Label(text='Email:')
label_email.pack(padx=5, pady=5)

email = tk.StringVar()
email_entry = tk.Entry(textvariable=email)
email_entry.pack()
email_entry.focus() # do il focus a questo campo

# creo widget di tipo ENTRY per far inserire un valore all'utente
label_password = tk.Label(text='Password:')
label_password.pack(padx=5, pady=5)

password = tk.StringVar()
passwrod_entry = tk.Entry(textvariable=password, show='*')
passwrod_entry.pack(padx=5, pady=5)

# creo il button per il login
btn_login = tk.Button(text='Login', command=login).pack()

# creo un widget di tipo COMBOBOX
mese_selezionato = tk.StringVar()
combo_mesi = ttk.Combobox(textvariable=mese_selezionato)
combo_mesi.pack(fill='x', pady=20, padx=50)
combo_mesi['values'] = [month_name[m] for m in range(1,13)] # presi dal modulo importato
combo_mesi['state'] = 'readonly' # per fare in modo che io non possa scrivere nella combo

combo_mesi.bind('<<ComboboxSelected>>', sleeziona_mese)

# creo widget di tipo BUTTON con qualche proprietà (molto simili alle label) e un comando in linea (lambda)
bottone_quit = tk.Button(text='Esci', width=10, height=2, borderwidth=3, command=lambda: finestra.quit())
bottone_quit.pack()

# window.mainloop() dice a Python di eseguire il ciclo degli eventi di Tkinter. 
finestra.mainloop()
