#Esercizio 003 di https://www.programmareinpython.it/esercizi-python/

#creo una lista vuota
lista = []

#chiedo quanti numeri voglio inserire
n = int(input('Quanti numeri vuoi inserire?'))

#itero per il range
for i in range(0, n):
    elemento = int(input())
    #aggiungo l'elemento alla lista
    lista.append(elemento)

#calcolo il numero maggiore
numero_maggiore = lista[0]
for numero in lista:
    if numero > numero_maggiore:
        numero_maggiore = numero
print('Il numero maggiore tra tutti è:', numero_maggiore)

