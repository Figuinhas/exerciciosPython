lista = []
cont = 0
while True:
    s = int(input('Digite um numero: '))
    lista.append(s)
    cont += 1
    desj = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while desj != 'S' and desj != 'N':
        desj = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if desj == 'N':
        break
list1 = sorted(lista)
rev = list(reversed(list1))
print(f'Foram digitados {cont} numeros.')
print(f'A lista em ordem decrescente é {rev}')
if 5 in lista:
    print('O numero 5 foi digitado!')
else:
    print('O numero 5 não foi digitado!')