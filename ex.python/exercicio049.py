print('=$'*15)
print('Tabuadinha dos crias')
print('=$'*15)
num = int(input('Digite um numero: '))
print('Está tabuada vai até o 10.')
for c in range(1,11):
    print('{} x {} = {}'.format(num,c,(num*c)))