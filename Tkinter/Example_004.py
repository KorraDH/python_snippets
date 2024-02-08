## Canale Youtube di Edoardo Midali (codegrind.it)
## Raccolta di vari esempi per creare finestre e gestire FRAME

import tkinter as tk    #importo il odulo base di Tkinter
from tkinter import ttk #ttk è il sub-modulo per la grafica più moderna

#--> FINESTRA PRINCIPALE
finestra = tk.Tk()
finestra.title('Esempio numero 003')
finestra.geometry('1024x768')

ico_importa = tk.PhotoImage(file='./Tkinter/import.png')
ico_programma = tk.PhotoImage(file='./Tkinter/programma.png')

finestra.iconphoto(True, ico_programma)

def login():
    print(email_entry.get())
    print(passwrod_entry.get())

# creo 3 frame all'interno della finestra principale (finestra), il 3° è un LabelFrame nel senso che ha anche un titolo
frame1 = tk.Frame(finestra, background='red', padx=10, pady=10, height=100, width=400)
frame2 = tk.Frame(finestra, background='yellow', padx=10, pady=10, height=100, width=400)
frame3 = tk.LabelFrame(finestra, background='orange', text='Sono un LabelFrame', padx=10, pady=10, height=100, width=400)
frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
#frame1.pack(fill='x', expand=True) #espando la dimensione come tutta la finestra in orizzontale

# creo widget e li assegno ai frame creati pocanzi
button1 = tk.Button(frame1, text='Ciao!')
button2 = tk.Button(frame2, text='Salve!')
button3 = tk.Button(frame3, text='Arrivederci!')

button1.pack()
button2.pack()
button3.pack()

# window.mainloop() dice a Python di eseguire il ciclo degli eventi di Tkinter. 
finestra.mainloop()
