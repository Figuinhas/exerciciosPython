from time import sleep
lop = ''
maior = []
num1 = int(input('Digite o 1º valor: '))
num2 = int(input('Digite o 2º valor: '))
while lop != 5:
    maior.append(num1)
    maior.append(num2)
    lop = int(input('''O que você deseja fazer com esses valores?
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa
    Opção: '''))
    soma = num1 + num2
    mult = num1*num2
    if lop == 1:
        #lop = 4
        print('§-'*10)
        print('A soma entre eles é {}'.format(soma))
        print('§-'*10)
    if lop == 2:
        print('§-'*10)
        print('{} x {} = {}'.format(num1,num2,mult))
        print('§-'*10)
        #lop = 4
    if lop == 3:
        print('§-'*10)
        print('O maior numero entre eles é {}'.format(max(maior)))
        print('§-'*10)
        #lop = 4
    if lop == 4:
        num1 = int(input('Digite o 1º valor: '))
        num2 = int(input('Digite o 2º valor: '))
    if lop > 5:
        print('Opção invalida, tente novamente')
print('Finalizando...')
sleep(2.5)
print('Fim')