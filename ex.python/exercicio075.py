n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um number: '))
n4 = int(input('Tecle o final number: '))
num = (n1,n2,n3,n4)
num1 = []
print(f'Você digitou os numeros {num}')
if 3 in num:
    posiçao_3 = num.index(3)
    print(f'o numero 3 aparece na {(posiçao_3)+1}ª posição')
if 9 in num:
    print(f'O valor 9 apareceu {num.count(9)} vezes')
else:
    print('O numero 9 aparece 0 vezes')
for c in num:
    if c % 2 == 0:
        num1.append(c)
print(f'Os numeros pares são {num1}')