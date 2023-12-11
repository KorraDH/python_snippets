#Esercizio 006 di https://www.programmareinpython.it/esercizi-python/

#creo una lista vuota
lista = []

#chiedo quanti numeri voglio inserire
n = int(input('Quanti numeri vuoi inserire?'))

#itero per il range
for i in range(0, n):
    elemento = int(input())
    #aggiungo l'elemento alla lista
    lista.append(elemento)

#calcolo la moltiplicazione
molt = 1
for numero in lista:
    molt = molt * numero
print('La moltiplicazione è:', molt)
