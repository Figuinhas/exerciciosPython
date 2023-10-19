import datetime
ano = int(input('Em qual ano você está?'))
p4 = ano % 4
p100 = ano % 100
p400 = ano % 400

if (p4 == 0 and p100 != 0) or (p400 == 0):
    print('é bissexto')
else:
    print('nao é bissexto')

