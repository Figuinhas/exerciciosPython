listapar = []
lista = []
soma = 0
somapar = 0
somatodos = 0
num = int(input('Até qual numero você deseja contar? '))

for c in range(1,num+1):
    if c%2 != 0:
        soma = soma + c
        lista.append(c)
    elif c%2 == 0:
        somapar = somapar + c
        listapar.append(c)
    somatodos = somapar + soma
print('Os impares são {}, e os pares são {}'.format(lista, listapar))
print('A soma dos impares resulta em {} e a soma dos pares resulta em {}'.format(soma,somapar))
print('E a soma de todos os numeros resulta em {}'.format(somatodos))