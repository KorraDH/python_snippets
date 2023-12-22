'''
Esercizio 024 di https://www.programmareinpython.it/esercizi-python/
Scrivi una funzione che crei una tupla contenente i nomi dei pianeti del sistema solare, 
la loro tipologia (gassoso o roccioso) e il numero di satelliti naturali conosciuti. 
Il programma deve quindi stampare a schermo il contenuto della tupla e il numero totale di satelliti.
'''

pianeti = (('Mercurio', 'roccioso', 0)
           , ('Venere', 'roccioso', 0)
           , ('Terra', 'roccioso', 1)
           , ('Marte', 'roccioso', 2)
           , ('Giove', 'gassoso', 95)
           , ('Saturno', 'gassoso', 83)
           , ('Urano', 'gassoso', 27)
           , ('Nettuno', 'gassoso', 14)
           )

print(type(pianeti)) #lo uso per vedere che tipo di oggetto è

def info_pianeti():
    #stampa a schermo l'elenco dei pianeti
    print("I pianeti del sistema solare sono:")
    for pianeta in pianeti:
        print(f"{pianeta[0]}: {pianeta[1]}, {pianeta[2]} satelliti")

    #calcola e stampa il numero di satelliti naturali totali
    num_satelliti = sum([pianeta[2] for pianeta in pianeti])

    print(f"Il numero totale di satelliti naturali conosciuti nel Sistema Solare è di: {num_satelliti}")

info_pianeti()

'''
#identico esercizio ma con una lista

pianeti_ls = list(pianeti) #conversione da tupla in lista

print(type(pianeti_ls)) #lo uso per vedere che tipo di oggetto è

def info_pianeti_ls():
    #stampa a schermo l'elenco dei pianeti
    print("I pianeti del sistema solare sono:")
    for pianeta_ls in pianeti_ls:
        print(f"{pianeta_ls[0]}: {pianeta_ls[1]}, {pianeta_ls[2]} satelliti")

    #calcola e stampa il numero di satelliti naturali totali
    num_satelliti_ls = sum([pianeta_ls[2] for pianeta_ls in pianeti_ls])

    print(f"Il numero totale di satelliti naturali conosciuti nel Sistema Solare è di: {num_satelliti_ls}")

info_pianeti_ls()
'''