'''
Esercizio 025 di https://www.programmareinpython.it/esercizi-python/
Scrivi una funzione che prenda come argomento un set di sport preferiti dall'utente 
e stampi un messaggio di testo che indica se si tratta di uno sport di squadra o individuale.
'''

def sport(sport_preferito):
    sport_individuale = {"tennis", "ping pong", "nuoto", "ciclismo"}
    sport_squadra = {"pallavolo", "calcio", "basket", "padel"}

    if sport_preferito.lower() in sport_individuale:
        print(f"Lo sport {sport_preferito} è uno sport individuale!")
    
    elif sport_preferito.lower() in sport_squadra:
        print(f"Lo sport {sport_preferito} è uno sport di squadra!")

    else:
        print("Non conosco questo sport!")

sport("PALLAVOLO")
