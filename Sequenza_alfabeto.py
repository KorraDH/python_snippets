import time

alfabeto = 'abcdefghilmnopqrstuvz'
ask_pos = input('Inserisci una lettera, ti dirò in che posizione si trova: ')
ask_pos_lc = ask_pos.lower() #converto in minuscolo
pos = 1

for char in alfabeto :
    if char == ask_pos_lc :
        break
    print(pos)
    time.sleep(0.5)
    pos = pos+1

# pos_char = chr(pos)
# print(pos)
# print(str(pos))
print('La lettera è in posizione: ' + str(pos))
    