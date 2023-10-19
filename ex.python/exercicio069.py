print('=-'*20)
print('CADASTRE UMA PEOPLE')
print('=-'*20)
p18 = 0
homens = 0
mulheres_20 = 0
while True:
    id = int(input('Idade: '))
    sex = str(input('Sexo: [M/F]')).upper().strip()[0]
    while sex != 'M' and sex != 'F':
        sex = str(input('Sexo: [M/F]')).upper().strip()[0]
    if id > 18:
        p18 += 1
    if sex == 'M':
        homens += 1
    if sex == 'F' and id < 20:
        mulheres_20 += 1
    print('=-' * 20)
    seq = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while seq != 'S' and seq != 'N':
        seq = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if seq == 'N':
        break
print('=-'*20)
print(f'{p18} pessoas tem mais de 18 anos.')
print('=-'*20)
print(f'{homens} homens foram cadastrados.')
print('=-'*20)
print(f'{mulheres_20} mulheres com menos de 20 anos foram cadastradas.')
print('=-'*20)
