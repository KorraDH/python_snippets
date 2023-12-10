#Esercizio 003 di https://www.programmareinpython.it/esercizi-python/

lista = [42, 55, 98, 11, 15, 54, 32]
numero_maggiore = lista[0]
for numero in lista:
    if numero > numero_maggiore:
        numero_maggiore = numero
print('Il numero maggiore tra tutti è:', numero_maggiore)

