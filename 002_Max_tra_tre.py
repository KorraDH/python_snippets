print('Inserisci tre numeri, ti dirò il più grande')

#se metto int prima dell'input obbligo ad inserire un intero
x = int(input('Primo numero: '))
y = int(input('Secondo numero: '))
z = int(input('Terzo numero: '))

if x >= y and x >= z:
    print('il numero più grande è: ' + str(x))
elif y >= x and y >= z:
    print('il numero più grande è: ' + str(y))
else :
    print('il numero più grande è: ' + str(z))
