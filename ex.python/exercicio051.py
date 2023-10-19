termo = int(input('Qual é o primeiro termo: '))
razao = int(input('Qual é a razão: '))
for c in range(1,11):
    pa = termo + (c-1)*razao #formula pa      an = a1 + (n-1)*r
    print(pa)
#CÒDIGO DO MANO GUANABAS
#primeiro = int(input('Primeiro termo: '))
#razao = int(input('Razao: '))
#decimo_termo = primeiro + (10-1)*razao
#for c in range(primeiro, decimo_termo + razao,razao):
    #print('{}'.format(c),end=  '--> ')
#print('FINISH')
