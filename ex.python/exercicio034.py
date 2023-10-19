salario = float(input('Qual seu salário?'))
dez = salario+salario*(10/100)
quinze = salario+salario*(15/100)
if salario > 1250.0:
    print('Você receberá um aumento de 10%, e seu salário atual será de {}'.format(dez))
else:
    print('Você receberá um aumento de 15%, e seu salário atual será de {}'.format(quinze))
