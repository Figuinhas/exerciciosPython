co = float(input('Cateto oposto:'))
ca = float(input('Cateto adjacente:'))
hip = ((ca**2) + (co**2))**(1/2)
print('Seu cateto oposto é {:.2f}, seu cateto adjacente é {:.2f}, logo sua hipotenusa é {:.2f}'.format(co,ca,hip))
