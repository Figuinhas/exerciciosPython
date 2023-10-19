s = 0
for c in range(1,6):
    n = int(input('Digite o {}° valor: '.format(c)))
    s = s + n  #toda vez que digitarem um numero, esse numero será somado a variavel s
print('O somatório de todos os valores foi {}'.format(s))
print(c) #o c é o numero de vezes que será repetido