city = str(input('Qual nome da sua cidade:'))
aa = city.upper().split()
firstname = 'SANTO' in aa
print('Sua cidade começa com o nome {}?{}'.format('SANTO',firstname))