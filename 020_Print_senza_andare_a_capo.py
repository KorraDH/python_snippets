'''
Esercizio 020 di https://www.programmareinpython.it/esercizi-python/
Scrivi una funzione che prenda una serie di input dall'utente utilizzando un ciclo while e li stampi con la funzione print senza andare a capo. 
Il ciclo while si deve interrompere quando l'utente preme INVIO senza scrivere nulla.

Che utilità ha quest'esercizio ? (ndr)
'''

def stampa():
    input_ut = input("Inserisci un valore (interrompi con invio doppio): ")
    while input_ut != "":
        print(input_ut, end=" ") #con end aggiungo una desinenza alla stringa
        input_ut = input("Inserisci un valore (interrompi con invio doppio): ")

stampa()
    