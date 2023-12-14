#Esercizio 012 di https://www.programmareinpython.it/esercizi-python/
#Scrivi una funzione che, dato in ingresso un valore espresso in metri, mandi in print l'equivalente in miglia terrestri, iarde, piedi e pollici.

#Definisco la funzione
def convertitore(valore):
	matrix = {}
	matrix["miglia"] = valore / 1609.344
	matrix["piedi"] = metri * 3.280840
	matrix["pollici"] = metri * 39.37008
	matrix["iarde"] = metri * 1.093613
	return matrix

#print("Inserisci i metri:")
metri = int(input("Inserisci i metri:"))

risultato = convertitore (metri)

print("a " + str(metri) + " metri corrispondono:")
for key, value in risultato.items():
	print(f"{key}: {value}")
