#Esercizio 013 di https://www.programmareinpython.it/esercizi-python/
#Scrivi una funzione che converta un dato numero di giorni, ore e minuti,
#passati dall'utente tramite funzione input, in secondi.

#Definisco la funzione
def calcola_secondi():
	print("Questa funzione calcola il numero di secondi dati giorni, ore e minuti")
	giorni = int(input("Inserisci il numero di giorni: ")) * 24 * 3600
	ore = int(input("Inserisci il numero di ore: ")) * 3600
        minuti = int(input("Inserisci il numero di minuti: ")) * 60
	totale = giorni + ore + minuti
	print(totale + " secondi")
