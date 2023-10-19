import random
import time
itens = ('Pedra', 'Papel','Tesoura')
pc = random.randint(0,2)
print('''Suas escolha:
[0] PEDRA
[1] PAPEL 
[2] TESOURA''')
jogador = int(input('Qual é a sua play? '))
print(f'Computador jogou: {itens[pc]}')
print(f'Jogador jogou: {itens[jogador]}')
if pc == 0: #pc jogou pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('jogador vence')
    elif jogador == 2:
        print('Computador venceu')
    else:
        print('Jogada invalida')
if pc == 1: #pc jogou papel
    if jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('jogador vence')
    elif jogador == 0:
        print('Computador venceu')
    else:
        print('Jogada invalida')
if pc == 2: #pc jogou tesoura
    if jogador == 2:
        print('Empate')
    elif jogador == 0:
        print('jogador vence')
    elif jogador == 1:
        print('Computador venceu')
    else:
        print('Jogada invalida')