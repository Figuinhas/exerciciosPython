v = int(input('Qual a velocidade do carro?'))
if v > 80:
    print('Perdeu veinho, foi multado, da próxima tampa a placa burrão')
    vp = (v - 80)*7
    print('Agora vai ter que pagar uma multinha coisas leves de apenas {} R$'.format(vp))
else:
    print('Ta suave patrão pode continuar rodando, tmj!')

