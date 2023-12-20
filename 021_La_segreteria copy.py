'''
Esercizio 021 di https://www.programmareinpython.it/esercizi-python/
Scrivi una funzione che accetti una lista di dizionari rappresentante una scuola. 
Ogni dizionario rappresenta uno studente e contiene nome, cognome, classe e voti. 
La funzione deve stampare un elenco di tutti gli studenti e calcolare la media dei voti di ciascuno.
'''

def segreteria(studenti):
    for studente in studenti:                                               #per ogni studente
        media_voti = sum(studente["voti"]) / float(len(studente["voti"]))   #calcolo la media voti
        studente["media"] = media_voti                                      #assegno la media voti al dizionario
    return studenti

#riempio il dizionario

studenti = [
    {"nome": "Mario", "cognome": "Rossi", "classe": "3B", "voti": [6, 7, 8, 6]},
    {"nome": "Luigi", "cognome": "Bianchi", "classe": "3A", "voti": [5, 7, 7, 6, 5]},
    {"nome": "Franco", "cognome": "Bugnano", "classe": "3B", "voti": [7, 7, 8, 6, 7.5]},
]

registro_segreteria = segreteria(studenti)
for elemento in registro_segreteria:
    print(elemento)