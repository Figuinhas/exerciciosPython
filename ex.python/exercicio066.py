cont = 0
soma = 0
while True:
    n = int(input('Digite um numero [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou {cont} numeros e a soma deles é {soma}')
