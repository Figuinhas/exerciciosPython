#VAI SE FODER NAO CONSEGUI ESSA MERDA
#código do guanabas
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} e {}'.format(t1,t2))
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(t3,'', end='')
    t1 = t2
    t2 = t3
    cont += 1
