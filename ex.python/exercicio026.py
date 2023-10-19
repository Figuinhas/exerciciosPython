frase = str(input('Digite uma frase:')).upper().strip()
fraseup = frase
fa = fraseup.count('A')
fe = fraseup.find('A') + 1
fl = fraseup.rfind('A') + 1
print('A letra aparece',fa, 'vezes')
print('Aparece a primeira vez na posição:',fe)
print('Aparece na ultima vez na posição:',fl)
