from datetime import date
name = str(input('Qual seu nome?'))
print('Olá {}, muito prazer!'.format(name))
genero = int(input('''Selecione o nº que corresponde ao seu genero: 
[1] Feminino
[2] Masculino
Qual seu genero?'''))
#ano = int(input('Em qual ano você nasceu?'))
if genero == 1:
    print('Você é do sexo feminino e não precisa fazer o alistamento obrigatório, até mais!')

if genero == 2:
    ano = int(input('Em qual ano você nasceu?'))
    atual = date.today().year
    idade = atual - ano
    dif = idade - 18
    # anoalistamento = 18+ano ------> ano que você devera se alistar
    dif1 = 18 - idade
    if idade > 18 and genero == 2:
        print('Você tem {} anos de idade e já passou {} anos do prazo do seu alistamento,\ncaso não tenha feito isso ainda, corre na junta pra arrumar isso'.format(idade,dif))
    elif idade < 18 and genero == 2:
        print('Você tem {} anos de idade, e faltam {} anos para voce se alistar'.format(idade,dif1))
    elif idade == 18 and genero == 2:
        print('Você tem 18 anos e está no ano de alistamento, corre na junta!')
