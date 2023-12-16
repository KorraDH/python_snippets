#Esercizio 014 di https://www.programmareinpython.it/esercizi-python/
#Scrivi un programma che, a scelta dell'utente, calcoli l'area di:
#- un cerchio
#- un quadrato
#- un rettangolo
#- un triangolo

print("""
Benvenuti nella programma "Geometra!"
Quale area vuoi calcolare ?
1 - Quadrato
2 - Rettangolo
3 - Trinagolo
4 - Cerchio
""")

print("Di quale figura geometrica vuoi calcolare l'area?")
scelta = int(input(">>> "))
if scelta == 1:
        print("Hai scelto: Area del quadrato")
        lato = float(input("Inserisci il valore del lato del quadrato "))
        print(f"L'area del quadrato è di: {lato * lato}")
elif scelta == 2:
        print("Hai scelto: Area del rettangolo")
        lato1 = float(input("Inserisci il valore del lato più lungo "))
        lato2 = float(input("adesso il valore del lato più corto "))
        print(f"L'area del rettangolo è di: {lato1 * lato2}")
elif scelta == 3:
        print("Hai scelto: Area del triangolo")
        base = float(input("Inserisci il valore della base "))
        altezza = float(input("adesso il valore dell'altezza "))
        print(f"L'area del triangolo è di: {(base * altezza) / 2}")
elif scelta == 4:
        print("Hai scelto: Area del cerchio")
        raggio = float(input("Inserisci il valore del raggio "))
        print(f"L'area del cerchio è di: {(raggio * raggio) * 3.14}")
else:
        print ("Nessun calcolo disponibile per la scelta effettuata")
