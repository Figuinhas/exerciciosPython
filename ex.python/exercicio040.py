n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
m = (n1+n2)/2
if m < 5.0:
    print('Sua média foi {}, e você está reprovado!'.format(m))
elif m >= 5.0 and m < 6.9:
    print('Sua média foi {}, e você está de recuperação'.format(m))
elif m >= 7.0:
    print('Sua média foi {}, e você está aprovado, parabéns!!!'.format(m))
print('Até mais!')

