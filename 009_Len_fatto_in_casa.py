#Esercizio 009 di https://www.programmareinpython.it/esercizi-python/
def lunghezza(lst_or_str):
    lunghezza = 0
    for unita in lst_or_str:
        lunghezza = lunghezza + 1
    return lunghezza
