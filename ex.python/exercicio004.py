n1 = input('Digite alguma coisa:')
print('Qual tipo primitivo desse valor?',type(n1))
print('Ele tem espaços?', n1.isspace())
print('Ele é um numero?', n1.isnumeric())
print('Ele é alfabético?', n1.isalpha())
print('Ele é alfanumerico?', n1.isalnum())
print('Ele está em maiusculas?' ,n1.isupper())
print('Ele está em minusculas?', n1.islower())
print('Está capitalizada?', n1.isascii())