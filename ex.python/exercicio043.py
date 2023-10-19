import time
name = str(input('Qual seu nome? '))
print('Olá {}, prazer em te conhecer!'.format(name))
altura = float(input('Me diga sua altura em metros: '))
print('Anotado!')
peso = float(input('Agora me diga seu peso em kg: '))
imc = peso/(altura**2)
print('Calculando...')
time.sleep(3)
if imc < 18.5:
    print('Seu IMC é {:.1f} e você está abaixo do peso ideal'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.1f} e você está com o peso ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.1f} e você está em sobrepeso'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.1f} e você está em obesidade'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.1f} e você está em obesidade mórbida, cuidado!'.format(imc))
