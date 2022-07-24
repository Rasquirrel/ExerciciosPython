"""
Progama desenvolvido por José Isac
24 de julho, 11:21AM
"""

# Dicionário de cores utilizado apenas para deixar o progama mais agradavel.

cores = {'Roxa-N': '\033[1;35m',
         'Roxa': '\033[35m',
         'Ciano': '\033[36m',
         'Ciano-N': '\033[1;36m',
         'Azul-N': '\033[1;34m',
         'Azul': '\033[34m',
         'Verde': '\033[32m',
         'Verde-N': '\033[1;32m',
         'Amarelo': '\033[33m',
         'Amarelo-N': '\033[1;33m',
         'Vermelho': '\033[31m',
         'Vermelho-N': '\033[1;31m',
         'Close': '\033[m'}

# Cabeçalho

print('{}-='.format(cores['Roxa-N'], cores['Close']) * 50, '\033[m')
print('{}DESAFIO N°36{}'.format(cores['Ciano-N'], cores['Close']))
print('{}Escreva um progama para aprovar o empréstimo bancário para a compra de uma casa.\n'
      'O progama vai perguntar o valor da casa, o salário do comprador e em quantos anos\n'
      'ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder\n'
      '30% do salário ou então o empréstimo será negado.{}'.format(cores['Amarelo'], cores['Close']))
print('{}-='.format(cores['Roxa-N']) * 50, '\033[m')

# Inicio

valorCasa = float(input('{}VALOR DA CASA:{} {}R${}'
                        ''.format(cores['Azul-N'], cores['Close'], cores['Amarelo-N'], cores['Close'])))
salarioComprador = float(input('{}SALARIO DO COMPRADOR: {}R${}'
                               ''.format(cores['Azul-N'], cores['Amarelo-N'], cores['Close'])))
periodoPagamento = int(input('{}PAGAR EM QUANTOS ANOS: '.format(cores['Azul-N'])))

quantMeses = periodoPagamento * 12
parcelaValor = valorCasa / quantMeses
limit = (30/100) * salarioComprador

if limit >= parcelaValor:
    print('{}EMPRÉSTIMO PERMITIDO!{}'.format(cores['Verde-N'], cores['Close']))
    print('{}PRESTAÇÃO MENSAL DE {}R${:.2f} {}POR {} MESES({} ANOS)'
          ''.format(cores['Azul-N'], cores['Amarelo-N'], parcelaValor, cores['Azul-N'], quantMeses, periodoPagamento))
else:
    print('{}EMPRÉSTIMO NEGADO POIS A PRESTAÇÃO DE {}R${:.2f} {}EXCEDE MAIS DE 30% DO VALOR'
          ' DO SEU SALÁRIO DE R${:.2f}'
          ''.format(cores['Vermelho-N'], cores['Amarelo-N'], parcelaValor, cores['Azul-N'], salarioComprador))
