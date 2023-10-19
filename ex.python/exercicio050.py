somapar = 0
somaimp = 0
cont_imp = 0
cont_par = 0
for c in range(1,7):
    num = int(input('Digite o {}° numero: '.format(c)))
    if num%2 == 0:
        somapar = somapar + num
        cont_imp = cont_imp + 1
        print('é par')
    elif num%2 != 0:
        somaimp = somaimp + num
        cont_par = cont_par + 1
        print('é impar')
print('Dentre os numeros que você escolheu,\n {} são pares e a soma deles resulta em {}, {} são impares e a soma deles resulta em {}.'.format(cont_par,somapar,cont_imp,somaimp))