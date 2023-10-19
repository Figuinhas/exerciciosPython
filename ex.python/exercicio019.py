# random

#al1 = input('Qual nome do primeiro aluno?')
#al2 = input('Qual nome do segundo aluno?')
#al3 = input('Qual nome do terceiro aluno?')
#al4 = input('Qual nome do quarto aluno?')
#sorteado = random.randint(1,4)
#print('O aluno sorteado é o aluno de numéro {}, Congrats!'.format(sorteado))
import random
a1 = input('Qual nome do primeiro aluno?')
a2 = input('Qual nome do segundo aluno?')
a3 = input('Qual nome do terceiro aluno?')
a4 = input ('Qual nome do quarto aluno?')
lista = [a1,a2,a3,a4]
escolhido = random.choice(lista)
print('O aluno escolhido é o (a) {}'.format(escolhido))
