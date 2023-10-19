import datetime
name = str(input('Qual seu nome?'))
print('Olá {}, muito prazer!'.format(name))
ano = int(input('Em qual ano você nasceu?'))
atual = datetime.date.today().year
idade =atual-ano
if idade <= 9:
    print('Você tem {} anos de idade, e está na categoria mirin'.format(idade))
elif idade >= 9: #and idade <= 14:
    print('Você tem {} anos de idade, e está na categoria infantil'.format(idade))
elif idade >= 14: #and idade <= 19:
    print('Você tem {} anos de idade, e está na categoria Junior'.format(idade))
elif idade >= 19: #and idade <= 25:
    print('Você tem {} anos de idade, e está na categoria Sênior'.format(idade))
elif idade > 25:
    print('Você tem {} anos de idade, e está na categoria Master'.format(idade))