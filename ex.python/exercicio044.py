import time
produto = float(input('Qual valor do produto? '))
vdc = produto - produto*(10/100)
vc = produto - produto*(5/100)
cc = produto
ccc = produto + produto*(20/100)
print("""Ok... 
      Nós temos as seguintes opções:
      - Opção 1: À vista no dinheiro ou cheque - 10% de desconto.
      - Opção 2: À vista no cartão - 5% de desconto.
      - Opção 3: Em até 2x no cartão - Valor normal do produto
      - Opção 4:  Em 3x ou mais no cartão - 20% de juros.""")
escolha = str(input('Qual forma de pagamento você escolhe? ')).upper()
print('Ok, aguarde alguns segundos...')
time.sleep(1)
print('Calculando...')
time.sleep(2)
if escolha == 'OPÇÃO 1':
    print('O valor a pagar que era R$ {}, agora é R$ {}'.format(produto,vdc))
elif escolha == 'OPÇÃO 2':
    print('O valor a pagar que era R$ {}, agora é R$ {}'.format(produto,vc))
elif escolha == 'OPÇÃO 3':
    print('O valor a pagar que era R$ {}, continua R$ {}'.format(produto,produto))
elif escolha == 'OPÇÃO 4':
    print('O valor a pagar que era R$ {}, agora é R$ {}'.format(produto,ccc))
