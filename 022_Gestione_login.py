'''
Esercizio 022 di https://www.programmareinpython.it/esercizi-python/
Scrivi un programma che crei un file CSV per memorizzare in un dizionario i dati degli utenti registrati su un sito web. 
I dati richiesti per ogni utente sono: username, password, email e data di registrazione.
Il programma deve permettere di salvare le informazioni nel file, leggere i dati e stamparli a schermo.
'''

import csv

def crea_file_csv(dizionario, nome_file):
    with open(nome_file, 'w', newline='') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(['username', 'password', 'email', 'data_iscrizione'])
        for utente in dizionario.values():
            writer.writerow([utente['username'], utente['password'], utente['email'], utente['data_iscrizione']])
    
def leggi_file_csv(nome_file):
    with open(nome_file, 'r') as file_csv:
        reader = csv.reader(file_csv)
        for row in reader:
            print(row)

#dizionario degli utenti:
utenti = {
    1: {'username': 'piero', 'password': 'p4ssw0rd', 'email': 'piero@gmail.com', 'data_iscrizione': '2023-01-01'},
    2: {'username': 'lisa', 'password': 's3cr3t', 'email': 'lisa@yahoo.com', 'data_iscrizione': '2023-01-02'},
    3: {'username': 'rita', 'password': 'p3ach', 'email': 'princess@castle.com', 'data_iscrizione': '2023-01-03'}
}

# Crea il file CSV
crea_file_csv(utenti, 'utenti.csv')

# Legge il file CSV e stampa i dati a schermo
leggi_file_csv('utenti.csv')