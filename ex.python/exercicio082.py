lista = []
lista_par = []
lista_impar = []
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    if n % 2 != 0:
        lista_impar.append(n)
    desj = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if desj != 'S' and desj != 'N':
        desj = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if desj == 'N':
        break
print(f'Os numeros digitados foram {lista}')
print(f'Os numeros pares digitados foram {lista_par}')
print(f'Os numeros impares digitados foram {lista_impar}')