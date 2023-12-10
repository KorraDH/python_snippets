carattere = input('Inserisci una lettera: ').lower()
vocali = 'aeiou'

if carattere in vocali:
	print("Il carattere " + carattere + " è una vocale")
else:
	print("Il carattere " + carattere + " non è una vocale")
