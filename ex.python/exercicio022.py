frase = str(input('Digite seu nome completo:'))
maxi = frase.upper()
min = frase.lower()
qnt = frase.split()
qnt1 = len(''.join(qnt))
#qntt = print(len(qnt1))
first = frase.split()
first1 = first[0]
firstname = len(first[0])
print('Olá {}, Prazer!\nSeu nome com todas as letras maiuscula è:{}'.format(frase,maxi))
print('Seu nome com todas as letras minusculas é:{}'.format(min))
print('Seu nome completo é composto por {} letras'.format(qnt1))
print('Seu primeiro nome é {}  e ele tem {} letras.'.format(first1,firstname))