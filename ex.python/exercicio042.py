#TRAVEI PRA CRL NISSO
a = float(input('Digite o valor do primeiro segmento: '))
b = float(input('Digite o valor do segundo segmento: '))
c = float(input('Digite o valor do terceiro segmento: '))
#naotri = (a+b < c) or (a+c < b) or (c+b < a)
#equilatero = (a==b) and (a==c)
#isóceles = (a==b) or (a==c) or (b==c)
#1escaleno = (a!=b) or (b!=c) or (a!=c)
if (a < b + c) and (b < a + c) and (c < + a +b):
    print('é triangulo')
    if (a==b) and (a==c):
        print('Equilatero')
    elif (a==b) or (a==c) or (b==c):
        print('Isóceles')
    else:
        print('Escaleno')
else:
    print('Não é triangulo')