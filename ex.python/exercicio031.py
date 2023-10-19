d = float(input('Qual vai ser a distancia da sua viagem em km:'))
pp1 = 0.50 * d
pp2 = 0.45 * d
if d > 200.0:
    print('Sua viagem custará {}'.format(pp2))
else:
    print('Sua viagem custará R$ {}'.format(pp1))
print('Boa viagem!')
