lista = []
maior = []
menor = []
for c in range(1,6):
    pesop = float(input('Digite em kg o peso da {}° pessoa: KG '.format(c)))
    lista.append(pesop)
print('Dentre os pesos citados, o maior é {} KG e o menor é {} KG.'.format(max(lista),min(lista)))