import colorsys
print('='*35)
print('Analisando se é triangulo ou não')
print('='*35)
a = float(input('Quanto mede o primeiro lado:'))
b = float(input('Quanto mede o segundo lado?'))
c = float(input('Quanto mede o terceiro lado?'))
if (a+b<c) or (a+c<b) or (c+b<a):
    print('não é triangulo essa porra!')
else:
    print('\033[0;37;40m é triangulo!')



