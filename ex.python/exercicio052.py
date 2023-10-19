num = int(input('Digite um numero para saber se o mesmo é primo ou não: '))
t = 0
cont = 0
for c in range(1, num + 1):
    if num%num == 0 and num%c == 0:
        t = t + 1 #sempre que um numero for divisivel por 1 ou por ele mesmo será somado 1 na variavel t, no final para ser primo, essa variavel n pode ser maior do que 2.

if t == 2:
    print('{} é divisivel apenas por {} e por {} logo ele è primo'.format(num,1,c))
else:
    print('O numero foi dividido {} vezes, logo, ele'.format(t))
    print('não é primo')