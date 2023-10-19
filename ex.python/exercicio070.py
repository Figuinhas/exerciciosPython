print('=-'*20)
print('HAHA WELCOME FIGAS STORE')
print('=-'*20)
mais_mil = 0
barato = []
tudo = 0
cont = 0
while True:
    nom_p = str(input('Nome do produto: '))
    preco_p = float(input('Preço do produto: R$ '))
    tudo += preco_p
    barato.append(preco_p)
    if preco_p > 1000:
        mais_mil += 1
        cont += 1
    seq = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while seq != 'S' and seq != 'N':
        seq = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if seq == 'N':
        break
print(f'Suas compras custaram um total de R$ {tudo}.')
print(f'Temos {mais_mil} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato custa R$ {min(barato)}')
#não consegui identificar o nome do produto mais barato fodase
#codigo do guanabas pra verificar menor preço e nome dele.
#if cont == 1 or preco < menor:
    #menor = preco
    #barato = produto
