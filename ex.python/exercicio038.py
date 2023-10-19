num1 = int(input('Qual primeiro numero?'))
num2 = int(input('Qual segundo numero?'))
if num1 > num2:
    print('O primeiro valor é {}, e ele é o maior entre eles'.format(num1))
elif num2 > num1:
    print('O segundo valor é {}, e ele é o maior entre eles'.format(num2))
else:
    print('Entre {} e {}, não existe valor maior, os dois são iguais'.format(num1,num2))
