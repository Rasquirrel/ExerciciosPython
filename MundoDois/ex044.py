# Exercício Python 44: 
# Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque = 10% de desconto
# à vista no cartao = 5% de desconto
# em até 2x no cartao = preço formal
# em até 3x ou mais no cartao = 20% de juros

print('=' * 20, 'LOJA', '=' * 26)
preco_Produto = float(input('DIGITE O PREÇO DO PRODUTO: \nR$'))

print('ESCOLHA A FORMA DE PAGAMENTO')
print('''[ 1 ] À VISTA DINHEIRO/CHEQUE
[ 2 ] À VISTA NO CARTAO
[ 3 ] EM ATÉ 2x NO CARTAO
[ 4 ] EM ATÉ 3x OU MAIS NO CARTAO
''')
print('=' * 52)
decisao = int(input())
print('=' * 52)

if decisao == 1:
    preco_NovoPreco = preco_Produto - (0.1 * preco_Produto)
    print(f'''O PRODUTO A SER COMPRADO CUSTA R${preco_Produto:,.2f} E O METODO
DE PAGAMENTO É À VISTA DINHEIRO/CHEQUE.
E POR ISSO VOCÊ RECEBE UM DESCONTO DE 10%.
O NOVO PRECO A SER NECESSÁRIO É DE R${preco_NovoPreco:,.2f} ''')
    print('=' * 52)

if decisao == 2:
    preco_NovoPreco = preco_Produto - (0.05 * preco_Produto)
    print(f'''O PRODUTO A SER COMPRADO CUSTA R${preco_Produto:,.2f} E O METODO
DE PAGAMENTO É À VISTA NO CARTAO.
E POR ISSO VOCÊ RECEBE UM DESCONTO DE 5%.
O NOVO PRECO A SER NECESSÁRIO É DE R${preco_NovoPreco:,.2f} ''')
    print('=' * 52)
