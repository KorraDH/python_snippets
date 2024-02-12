import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog

versione = 'versione 0.1.2 del 09-02-2024'

def importa_file():
    window_importa = ttk.Toplevel(root)
    window_importa.title("Importa file da terminalino")
    window_importa.geometry('640x480')
    window_importa.lift #la tengo in primo piano
    
    filepath = ''

    def seleziona_file():
        # definisco le estensioni possibili
        file_types = [("File di testo", "*.txt *.csv")]

        # chiedo di selezionare un file con le estensioni possibili
        filename = filedialog.askopenfilename(title='Seleziona un file', initialdir="/home", filetypes=file_types)
        
        # aggiorno la entry con il percorso
        ent_nomefile.delete(0, ttk.END)
        ent_nomefile.insert(0, filename)
    
    def importa_file():
        global data # dichiarando la variabile come globale posso utilizzarla anche fuori dalla funzione
        filepath = ent_nomefile.get()
        # testo se filepath è vuoto
        if not filepath:
            return
            
        #print('Inizio importazione dati')
        f = open(filepath, 'r')
        data = f.read()
        #print('Fine importazione dati') 
        fine = ttk.Label(window_importa, text='Importazione terminata!', background='green')
        fine.grid(column=0, row=3)
                        
    lbl_ins_path = ttk.Label(window_importa, text="Indica o seleziona il percorso del file")
    ent_nomefile = ttk.Entry(window_importa, width=50)
    btn_selezionafile = ttk.Button(window_importa, text='Apri file', command=seleziona_file)
    btn_importa = ttk.Button(window_importa, text='Importa dati', bootstyle='success', command=importa_file)
    btn_stampa = ttk.Button(window_importa, text='Stampa dati', command=lambda: print(data))
    
    lbl_ins_path.grid(column=0, row=0, padx=5, pady=5)
    ent_nomefile.grid(column=0, row=1, padx=5, pady=5)
    btn_selezionafile.grid(column=1, row=1, padx=5, pady=5)
    btn_importa.grid(column=0, row=2, padx=5, pady=5)
    btn_stampa.grid(column=1, row=2, padx=5, pady=5)

    # bind per uscire dalla maschera
    def on_key_press(event):
        if event.keysym == "Escape":
            window_importa.destroy()
    window_importa.bind("<KeyPress>", on_key_press)


def help():
    window_help = ttk.Toplevel(root)
    window_help.title("Informazioni sull'applicazione")
    
    lbl_immagine = ttk.Label(window_help, image=ico_programma)
    lbl_titolo = ttk.Label(window_help, text="Gestione verifiche capoturni")
    lbl_versione = ttk.Label(window_help, text=versione)
    lbl_crediti = ttk.Label(window_help, text="Copyright Corrado Bigliardi\nIter Innovation\nper Anofor Srl")

    lbl_immagine.grid(column=0, row=0 ,padx=5, pady=20)
    lbl_titolo.grid(column=0, row=1, padx=5, pady=5)
    lbl_versione.grid(column=0, row=2, padx=5, pady=5)
    lbl_crediti.grid(column=0, row=3, padx=5, pady=5)

    # bind per uscire dalla maschera
    def on_key_press(event):
        if event.keysym == "Escape":
            window_help.destroy()
    window_help.bind("<KeyPress>", on_key_press)

#--> FINESTRA PRINCIPALE
root = tk.Tk()
root.title('Gestione Verifiche Capoturni')
root.geometry('1366x768')
ico_programma = tk.PhotoImage(file='ANFGCO/Ghaphics/screwdriver.png')
root.iconphoto(True, ico_programma)

# definisco la griglia
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1) 
root.rowconfigure(1, weight=4)

# definisco i frame
filtri = ttk.LabelFrame(root, text="Filtri", borderwidth=2)
griglia = ttk.LabelFrame(root, text='Risultato', borderwidth=2)

# assegno i frame alla griglia
filtri.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)
griglia.grid(column=0, row=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

# aggiungo la menu bar
menubar = ttk.Menu(root)
root.config(menu=menubar)
# poi creo le voce di menù
menu_file = ttk.Menu(menubar, tearoff=0) # con il parametro tearoff=0 elimino la prima riga in alto
menu_help = ttk.Menu(menubar, tearoff=0)

# assegno alle voci al menu
menubar.add_cascade(label='File', menu=menu_file)
menubar.add_cascade(label='Help', menu=menu_help)

# creo i comandi sotto alle voci di menu
menu_anagrafiche = ttk.Menu(menu_file, tearoff=0)
menu_file.add_cascade(label='Anagrafiche', menu=menu_anagrafiche)
menu_anagrafiche.add_command(label='Stabilimenti', command='')
menu_anagrafiche.add_command(label='Turni', command='')
menu_anagrafiche.add_command(label='Controlli', command='')
menu_anagrafiche.add_command(label='Capiturno', command='')

menu_file.add_separator()
menu_file.add_command(label='Importa file da terminalino', command=importa_file)
menu_file.add_separator()
menu_file.add_command(label='Esci', command=root.quit)

menu_help.add_command(label='Informazioni sul programma', command=help)

# bind per uscire dalla maschera
def on_key_press(event):
    if event.keysym == "Escape":
        root.quit()
root.bind("<KeyPress>", on_key_press)

root.mainloop()