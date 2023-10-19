num = ('zero','um','dois','tres','quadro','cinco','seis','sete','oito','nove','dez','onze','doze','treze', 'quatorze','quize','dezesseis','dezessete','dezoito','dezenove','vinte')
digite = int(input('Digite um numero: [de 0 a 20]'))
while digite < 0 or digite > 20:
    digite = int(input('Digite um numero: [de 0 a 20]'))
print(f'Voce digitou o numero {num[digite]}.')