import random
print('=-'*20)
print('GO PLAYED PAR OU IMPAR VEINHO')
print('=-'*20)
pc = random.randint(1,10)
cont = 0
while True:
    n = int(input('Digite um valor: '))
    pi = str(input('Par ou impar? [P/I]')).strip().upper()[0]
    num = pc + n
    if num % 2 ==0:
        #print('Par')
        if pi == 'P':
            print('Você ganhou, continue!')
            cont += 1
        if pi == 'I':
            print('=-' * 35)
            print(f'O pc jogou {pc}, você jogou {n}. Total {num} deu par... você perdeu!')
            break
    if num % 2 != 0:
        #print('Impar')
        if pi == 'P':
            print('=-' * 35)
            print(f'O pc jogou {pc}, você jogou {n}. Total {num} deu impar... você perdeu!')
            break
        if pi == 'I':
            print('Você ganhou, continue!')
            cont += 1
print('=-'*35)
print(f'Perdeu veinho, você ganhou {cont} vezes consecutivas.')
print('=-'*35)