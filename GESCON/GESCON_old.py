# Con questo programma gestirò i controlli che il responsabile di reparto deve effettuare ad ogni turno
# Il programma si compone di
# - Anagrafica controlli
# - Lettura controlli da file di testo
# - Visualizzazione controlli
# - Analisi controlli mancanti

import tkinter as tk
from tkinter import ttk
import pyodbc

class DatabaseManager:
    def __init__(self):
        #configura la connessione al db
        #self.connection_string = 'DRIVER={SQL Server};SERVER=192.168.1.251;DATABASE=GESCON;UID=sa;PWD=12Iter34'
        self.connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.1.251;DATABASE=GESCON;UID=sa;PWD=12Iter34'
        self.connection = pyodbc.connect(self.connection_string)
        self.cursor = self.connection.cursor()

    def esegui_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()

    def recupera_dati(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()
    
class DatabaseManagementApp:
    def __init__(self, finestra_principale):
        self.finestra_principale = finestra_principale
        self.finestra_principale.title("ANOFOR - Gestione controlli")

        # Inizializza il gestore del database
        self.db_manager = DatabaseManager()

        # Frame per Anagrafica Stabilimenti
        self.frame_stabilimenti = ttk.Frame(finestra_principale, padding="10")
        self.frame_stabilimenti.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.create_stabilimenti_widgets()

        # Frame per Anagrafica Operatori
        self.frame_operatori = ttk.Frame(finestra_principale, padding="10")
        self.frame_operatori.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.create_operatori_widgets()

    def create_stabilimenti_widgets(self):
        ttk.Label(self.frame_stabilimenti, text="Anagrafica Stabilimenti").grid(row=0, column=0, columnspan=4)

    def create_operatori_widgets(self):
        ttk.Label(self.frame_operatori, text="Anagrafica Operatori").grid(row=0, column=0, columnspan=4)

if __name__ == "__main__":
    finestra_principale = tk.Tk()
    app = DatabaseManagementApp(finestra_principale)
    finestra_principale.mainloop()