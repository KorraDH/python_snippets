#Esercizio 015 di https://www.programmareinpython.it/esercizi-python/

import random

def gen_coppia():
        charset = "ABCDEF0123456789"
        stringa = ''
        for i in range(2):
            stringa = stringa + random.choice(charset)
        return stringa

mac_address5=''

for x in range(5):
      mac_address5 = mac_address5 + gen_coppia() + ':'

mac_address = mac_address5 + gen_coppia()

print(mac_address)
          