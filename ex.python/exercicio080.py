lista = []
for c in range(0,5):
    num = int(input('Digite um numero: '))
    if c == 0:
        lista.append(num)
        print(f'Adicionado na posição {c}')
    elif num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(f'Os valores adicionados foram {lista}')


