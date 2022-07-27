# Exercício Python 44: 
# Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque = 10% de desconto
# à vista no cartao = 5% de desconto
# em até 2x no cartao = preço formal
# em até 3x ou mais no cartao = 20% de juros

print('=' * 10, 'LOJA', '=' * 10)
preco_Produto = float(input('DIGITE O PREÇO DO PRODUTO: \nR$'))

print('ESCOLHA A FORMA DE PAGAMENTO')
print('''[ 1 ] À VISTA DINHEIRO/CHEQUE
[ 2 ] À VISTA NO CARTAO
[ 3 ] EM ATÉ 2x NO CARTAO
[ 4 ] EM ATÉ 3x OU MAIS NO CARTAO
''')
decisao = int(input())
