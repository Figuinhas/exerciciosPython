a = float(input('Qual a altura da parede?'))
l = float(input('Qual a largura da parede?'))
area = a*l
tinta = area/2
#Considerar que cada litro de tinta pinta 2m²
print('Sua area é de {} m², e você precisaria de {} Litros de tinta para pintar a parede por completo'.format(area,tinta))