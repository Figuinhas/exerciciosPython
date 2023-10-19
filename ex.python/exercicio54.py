import datetime
maior = 0
menor = 0
#lista_maior = []
#lista_menor = []
for c in range(1,8):
    p = int(input('Qual a data de nascimento da {}° pessoa?'.format(c)))
    idade = datetime.date.today().year - p
    print(idade)
    if idade >= 21: #se for maior ou = a 18 anos vai pra lista maior
        maior = maior + 1
        #lista_maior.append(c)
    else: # se nao vai pra lista menor
        menor = menor + 1
        #lista_menor.append(c)
#maio = len(lista_maior) #conta quantos itens tem na lista maior
#meno = len(lista_menor) #conta quantos itens tem na lista menor
print('Dessas pessoas, {} são maiores de idade, e {} são menores'.format(maior,menor))