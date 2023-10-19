import random
import time
num =random.randint(0,5)
print('='*70)
print('O computador irá gerar um número aleatório entre 0 e 5, tente adivinhar...')
print('='*70)
sorteado = int(input('Qual seu palpite?'))
print('PROCESSANDO...')
time.sleep(3)
if sorteado == num:
    print('Congrats veinho(a), you acertou em cheio!, ta com o cu pra lua mesmo')
else:
    print('SOOOOO CLOSEEE VEINHO, tenta depois blz!')
print('=========================================')
print('O numéro sorteado foi {}!'.format(num))
print('=========================================')