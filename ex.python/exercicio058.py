import random
pc = random.randint(1,10)
player = ''
tentativas = 0
print('-='*35)
print('Tente adivinhar o numero que a maquina irá gerar. (entre 1 e 10)')
print('-='*35)
while player != pc:
    player = int(input('Digite um numero: '))
    tentativas = tentativas + 1
    if player == pc:
        print('Você acertou o numero que a maquina pensou que foi {}, e você tentou {} vezes'.format(pc,tentativas))