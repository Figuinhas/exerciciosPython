n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
n3 = int(input('Digite mais um:'))
maior = max(n1,n2,n3)
menor = min(n1,n2,n3)
if maior:
    print('O maior numero entre {}, {} e {}, é no numero {}'. format(n1,n2,n3,maior))
else:
    print('O menor numero é {}'.format(menor))
print('E o menor numero é o {}'.format(menor))

