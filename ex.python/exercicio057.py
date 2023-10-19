s = 'M','F'
while s != 'M' and s != 'F':
    s = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if s != 'M' and s != 'F':
        print('Sexo não compreendido, tente novamente.')
print('Sexo {}, registrado com sucesso'.format(s))
