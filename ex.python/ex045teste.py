import time
import random
itens = ('Pedra','Papel','Tesoura')
pc = random.randint(0,2)
player = int(input('''Você tem as opções:
[0]
[1]
[2]
Qual será sua play?'''))
print('Pedra...')
time.sleep(1)
print('Papel...')
time.sleep(1)
print('Tesoura...')
time.sleep(1)
print('°'*40)
print('O computador jogou {}.'.format(itens[pc]))
print('Você jogou {}.'.format(itens[player]))
print('°'*40)
if player == 0: #se o jogador escolher pedra
    if pc == 0:
        print('Empate')
    elif pc == 1:
        print('Computador ganhou')
    elif pc == 2:
        print('Jogador ganhou')
elif player == 1: #se o jogador escolher papel
    if pc == 0:
        print('Jogador ganhou')
    elif pc == 1:
        print('Empate')
    elif pc == 2:
        print('Computador ganhou')

elif player == 2: #se o jogador escolher tesoura
    if pc == 0:
        print('Computador ganhou')
    elif pc == 1:
        print('Jogador ganhou')
    elif pc == 2:
        print('Empate')
else:
    print('Jogada invalide, tente novamente!')