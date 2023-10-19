lista = []
for num in range(0,5):
    lista.append(int(input(f'Digite um numero para a posição {num}: ')))
print(f'Você digitou os valores {lista}')
print(f'o maior valor foi {max(lista)} nas posições', end= ' ')
for c in range(0, len(lista)):
    if lista[c] == max(lista):
        print(c, end=' ')
print(f'\nO menor valor foi {min(lista)}, nas posições', end= ' ')
for m in range(0, len(lista)):
    if lista[m] == min(lista):
        print(m, end= ' ')
