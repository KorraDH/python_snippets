#Esercizio 010 di https://www.programmareinpython.it/esercizi-python/
#Scrivi una funzione che data in ingresso una lista A contenente n parole, restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.

#creo una lista vuota
lista = []

#chiedo quanti elemnti voglio inserire
n = int(input('Quanti elementi vuoi inserire? '))

#itero per il range
for i in range(0, n):
    elemento = input()
    #aggiungo l'elemento alla lista
    lista.append(elemento)

contatore = 0
#restituisco le lunghezze dei singoli elementi
for el in lista:
	contatore = contatore + 1
	print("La lunghezza della stringa numero: " + str(contatore) + " con valore " + el  + " è di " + str(len(el)) + " caratteri")

