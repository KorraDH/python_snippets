## Canale Youtube di Edoardo Midali (codegrind.it)
## Raccolta di vari esempi per creare finestre e gestirne il layout management con il metodo PACK

import tkinter as tk    #importo il odulo base di Tkinter
from tkinter import ttk #ttk è il sub-modulo per la grafica più moderna

#--> FINESTRA PRINCIPALE
finestra = tk.Tk()
finestra.title('Esempio numero 003')
finestra.geometry('1024x768')
ico_importa = tk.PhotoImage(file='./Tkinter/import.png')
ico_programma = tk.PhotoImage(file='./Tkinter/programma.png')
finestra.iconphoto(True, ico_programma)

#--> WIDGET
# Padding:
# padx e pady sono il pad AL DI FUORI dell'elemento mentre ipadyx e ipady sono i pad ALL'INTERNO dell'elemento
# nel pack posso mettere le proprietà fill ed expand.
# Il pack è sempre verticale a meno che non si specifichi la proprietà "side"

label1 = tk.Label(finestra, text='Testo 1', bg='green', fg='white')
label1.pack(padx=5, pady=2, ipadx=10, ipady=5, fill='x')

label2 = tk.Label(finestra, text='Testo 2', bg='orange', fg='white')
label2.pack(padx=5, pady=2, ipadx=10, ipady=5, fill='x')

label3 = tk.Label(finestra, text='Testo 3', bg='red', fg='white')
label3.pack(padx=5, pady=2, ipadx=10, ipady=5, fill='x')

label4 = tk.Label(finestra, text='Testo 4', bg='purple', fg='white')
label4.pack(padx=5, pady=2, ipadx=10, ipady=5, fill='both', expand=True, side='left')

label5 = tk.Label(finestra, text='Testo 5', bg='blue', fg='white')
label5.pack(padx=5, pady=2, ipadx=10, ipady=5, fill='both', expand=True, side='left')

label6 = tk.Label(finestra, text='Testo 6', bg='yellow', fg='white')
label6.pack(padx=5, pady=2, ipadx=10, ipady=5, fill='both', expand=True, side='left')

# window.mainloop() dice a Python di eseguire il ciclo degli eventi di Tkinter. 
finestra.mainloop()
