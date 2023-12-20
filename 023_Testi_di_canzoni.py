'''
Esercizio 023 di https://www.programmareinpython.it/esercizi-python/
Scrivi una funzione che permetta di inserire una canzone e salvarla in un file di testo. 
Il programma deve chiedere all'utente di inserire il titolo e il testo della canzone, 
e poi salvare quest'ultimo in un file intitolato titolo_canzone.txt.
'''

def salva_testo_canzone(titolo, testo):
    nome_file = titolo + '.txt'
    with open(nome_file, 'w') as file_testo:
        file_testo.write(testo)
    print(f"Testo della canzone '{titolo}' salvato in '{nome_file}'.")

titolo_canzone = input("Inserisci il titolo della canzone: ")
testo_canzone = input("Inserisci il testo della canzone: ")

salva_testo_canzone(titolo_canzone, testo_canzone)
