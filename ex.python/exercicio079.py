lista = []
n = int(input('Digite um numero: '))
lista.append(n)
while True:
    print('Adicionado com sucesso')
    quest = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if quest != 'S' and quest != 'N':
        quest = str(input('Deseja continuar?[S/N]')).upper().strip()[0]
    if quest == 'N':
            break
    m = int(input('Digite um numero: '))
    if m in lista:
        print('Valor duplicado, não vou adicionar')
    else:
        lista.append(m)
print(f'Você digitou os valres {sorted(lista)}')