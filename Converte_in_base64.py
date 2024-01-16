'''
Chiede una stringa e la converte in base64, comodo per gestire le autenticazioni SMTP
'''

import base64

stringa = input('Inserisci la stringa da codificare: ')

stringa_codificata = base64.b64encode(stringa.encode())

print(stringa_codificata)
