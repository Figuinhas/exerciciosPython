v = float(input('Qual valor do produto? R$'))
vd = v-v*(5/100)
print('Seu produto custa R${:.2f}, e o valor dele com 5% de desconto fica R$ {:.2f}'.format(v,vd))
