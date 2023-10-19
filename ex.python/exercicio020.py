from random import shuffle
a1 = input('Qual aluno de numero 1?')
a2 = input('Qual aluno de numero 2?')
a3 = input('Qual aluno de numero 3?')
a4 = input('Qual aluno de numero 4?')
lista = [a1,a2,a3,a4]
shuffle(lista)
print('Sua ordem será:')
print(lista)

