'''
Esercizio 019 di https://www.programmareinpython.it/esercizi-python/
Scrivi una funzione che aggiunga ad una lista 10 colori inseriti dall'utente. 
Il programma deve poi chiedere all'utente di inserire una lettera e mostrare in output 
solo i colori nella lista che iniziano con quella lettera.
'''

def colori():
    colors = []
    print("Inserisci i colori, conferma ogni colore con Invio, digita \"done\" quando terminato: ")
    while True:
        elemento = input(">>> ")
        if elemento == 'done':
            break
        colors.append(elemento.upper()) #metodo per aggiungere l'elemento alla lista; già che ci sono lo inserisco in maiuscolo così non ho poi problemi dopo nella ricerca
    
    print("I colori inseriti sono: ", colors)
    
    lettera = input("Inserisci la prima lettera del colore da ricercare: ")
    lettera = lettera.upper() #trasformo la lettera in maiuscolo così non ho problemi con la verifica

    for i in colors:
        if i.startswith(lettera):
            print(i)

colori()
    