expre = str(input('Digite a expressão: '))
abre = 0
fecha = 0
for simb in expre:
    if simb == '(':
        abre += 1
    elif simb == ')':
        fecha += 1
if abre == fecha:
    print('Expressão valida!')
else:
    print('Opção invalidade!')
