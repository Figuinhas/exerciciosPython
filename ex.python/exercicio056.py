#NÃO CONSEGUI ESSA PRRA TB
#CÓDIGO DO GUANABAS
somaidade = 0
media_idade = 0
maior_hom = 0
nome_homvei = ''
totmulher20 = 0
for p in range(1,5):
    print('------ {}ª Pessoa ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maior_hom = idade
        nome_homvei = nome
    if sexo in 'Mn' and idade > maior_hom:
        maior_hom = idade
        nome_homvei = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
media_idade = somaidade/4
print('A média de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_hom,nome_homvei))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))