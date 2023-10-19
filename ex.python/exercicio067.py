cont = 0
while True:
    t = int(input('Quer ver a tabuada de qual valor? '))
    if t < 0:
        break
    for cont in range(1,11):
        #cont += 1
        produto = t * cont
        print(f'{t} X {cont} = {produto}')
print('Valor invalido, Tabuada interrompida!')
