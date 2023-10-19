salario = float(input('Qual seu salário?'))
sa = salario+salario*(15/100)
print('Seu salário atual é de R${:.2f}, considerando que você terá um aumento de 15%, seu salário atual será de R$ {:.2f}'.format(salario,sa))
