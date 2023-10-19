media = []
lista = []
stop = ''
cont = 0
while stop != 'N':
    num = int(input('Digite um numero: '))
    media.append(num)
    lista.append(num)
    cont = cont + 1
    desejo = str(input('Deseja continuar? [S/N]')).upper()
    stop = desejo
    if stop == 'N':
        md = sum(media)/cont
        maior = max(lista)
        menor = min(lista)
        print('Você digitou {} numeros, a média entre eles é {}, o maior entre eles é {} e o menor entre eles é {}'.format(cont,md,maior,menor))
    #if stop != 'S' and stop != 'N':
        #print('Opção invalida, tente novamente')
#esse ultimo comando eh uma merda n funciona
