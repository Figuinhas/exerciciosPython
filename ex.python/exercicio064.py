cont = 0
num = ''
soma = 0
while num != 999:
    n = int(input('Digite um numero inteiro: '))
    print('Se desejar parar, digite 999')
    cont = cont + 1
    num = n
    if n != 999:
        soma += n
print(f'FIM... Você digitou um total de {cont-1} numeros e a soma deles resulta em {soma}')