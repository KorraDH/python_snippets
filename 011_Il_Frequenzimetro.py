#Esercizio 011 di https://www.programmareinpython.it/esercizi-python/
#Scrivi una funzione che, data una stringa come parametro, restituisca un dizionario rappresentante la "frequenza di comparsa" di ciascun carattere componente la stringa.

#Definisco la funzione
def frequenzimetro(stringa):
	matrix = {}
	for carattere in stringa:
		if carattere in matrix:
			matrix[carattere] += 1
		else:
			matrix[carattere] = 1
	return matrix

risultato = frequenzimetro ('adskjdfhhfdihhih')

print(risultato)
#print(matrix.items())
