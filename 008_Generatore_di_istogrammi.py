#Esercizio 008 di https://www.programmareinpython.it/esercizi-python/

#creo una lista vuota
lista = []

#chiedo quanti elemnti voglio inserire
n = int(input('Quanti elementi vuoi inserire? '))

#itero per il range
for i in range(0, n):
    elemento = int(input())
    #aggiungo l'elemento alla lista
    lista.append(elemento)

#disegno gli istogrammi
for val in lista:
    print("*" * val)
