termo = int(input('Qual é o primeiro termo: '))
razao = int(input('Qual é a razão: '))
qtt = int(input('Quantos termos você deseja ver?'))
cont = 0
while cont != qtt:
    cont = cont + 1
    pa = termo + (cont-1)*razao #formula pa      an = a1 + (n-1)*r
    print(pa)
    if cont == qtt:
        qt = int(input('Você deseja ver mais quantos termos? '))
        qtt = qtt + qt
        if qt == 0:
            print('FIM')
            print('Termos mostrados',cont)
#SOFRI PRA CONSEGUIR ESSE, ACHO QUE CONSEGUI NA SORTE!!