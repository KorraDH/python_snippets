#Esercizio 007 di https://www.programmareinpython.it/esercizi-python/

#creo una lista vuota
lista = []

#chiedo quanti elemnti voglio inserire
n = int(input('Quanti elementi vuoi inserire? '))

#itero per il range
for i in range(0, n):
    elemento = input()
    #aggiungo l'elemento alla lista
    lista.append(elemento)

#chiedo di passare un elemento da cercare
search = input('Indica un elemento da ricercare in lista ')

#verifico se l'elemento è presente in lista
trovato = False
for nome in lista:
    if nome == search:
        trovato = True
        break
if trovato:
    print(search + " è presente nella lista all'indice " + str(lista.index(search)) + " partendo da 0")
else:
    print("l'elemento " + search + " non è presente in lista")
