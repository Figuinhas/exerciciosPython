termo = int(input('Qual é o primeiro termo: '))
razao = int(input('Qual é a razão: '))
cont = 0
while cont != 10:
    cont = cont + 1
    pa = termo + (cont-1)*razao #formula pa      an = a1 + (n-1)*r
    print(pa ,'-> ', end='')
