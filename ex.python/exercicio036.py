casa = float(input('Valor da casa desejada:'))
salario = float(input('Seu salário é:'))
anos = int(input('Em quantos anos você deseja pagar?'))
valorcasa = casa/(anos*12)
print('Suas prestações ficaram em R${:.2f}'.format(valorcasa))

if valorcasa > (30/100)*salario:
    print('Infelizmente você é pobre e não pode lançar essa house')
elif valorcasa <= (30/100)*salario:
    print('Você pode realizar o empréstimo, pode dar andamento no processo.')
