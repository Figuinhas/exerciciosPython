nome = str(input('Qual é seu nome? '))
if nome == 'Guilherme'or nome == 'Figas':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular in Brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')

#else:
    #print('Seu nome é bem normal.')
print('Tenha um bom dia! {}'.format(nome))
