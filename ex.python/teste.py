#import emoji
#print(emoji.emojize("Olá rapeize :smiling_face_with_sunglasses:", language='alias'))
sacar = float(input('Qual valor você quer sacar? R$ '))
cont_50 = 0
cont_20 = 0
cont_10 = 0
cont_1 = 0
while True:
    if sacar > 50:
        cont_50 = sacar // 50
        sacar = sacar % 50
    if sacar > 20:
        cont_20 = sacar // 20
        sacar = sacar % 20
    if sacar > 10:
        cont_10 = sacar // 10
        sacar = sacar % 10
    if sacar > 1:
        cont_1 = sacar // 1
        sacar = sacar % 1
    if sacar < 1:
        print(f'O valor de R$ {sacar:.2f} não é possível sacar, e retornará para a sua conta!')
        break
if cont_50 > 0:
    print(f'Total de {cont_50} cédulas de R$ 50')
if cont_20 > 0:
    print(f'Total de {cont_20} cédulas de R$ 20')
if cont_10 > 0:
    print(f'Total de {cont_10} cédulas de R$ 10')
if cont_1 > 0:
    print(f'Total de {cont_1} cédulas de R$ 1')
print('=-'*20)
print('Obrigado e volte sempre fdp!')
