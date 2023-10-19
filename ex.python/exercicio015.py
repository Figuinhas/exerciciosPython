dias = int(input('Quantos dias de alguel?'))
km = float(input('Quantos km você rodou?'))
carrodia = float(60*dias)
kmrodado = float(0.15*km)
vt = kmrodado + carrodia
print('Utilizando o carro por {} dias, e rodando {} Km com ele, o valor total a pagar é de R$ {}'.format(dias,km,vt))