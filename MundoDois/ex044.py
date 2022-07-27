# Progama desenvolvido por José Isac
# 27 de julho, 10:12
# v1.0

print('=' * 20, ' LOJA ', '=' * 26)
preco_Produto = float(input('DIGITE O PREÇO DO PRODUTO: \nR$'))

print('ESCOLHA A FORMA DE PAGAMENTO')
print('''[ 1 ] À VISTA DINHEIRO/CHEQUE
[ 2 ] À VISTA NO CARTAO
[ 3 ] EM ATÉ 2x NO CARTAO
[ 4 ] EM ATÉ 3x OU MAIS NO CARTAO
''')
print('=' * 54)
decisao = int(input())
print('=' * 54)

if decisao == 1:
    preco_NovoPreco = preco_Produto - (0.1 * preco_Produto)
    print(f'''O PRODUTO A SER COMPRADO CUSTA R${preco_Produto:,.2f} E O METODO
DE PAGAMENTO É À VISTA DINHEIRO/CHEQUE.
E POR ISSO VOCÊ RECEBE UM DESCONTO DE 10%.
O NOVO PRECO A SER NECESSÁRIO É DE R${preco_NovoPreco:,.2f} ''')
    print('=' * 54)

elif decisao == 2:
    preco_NovoPreco = preco_Produto - (0.05 * preco_Produto)
    print(f'''O PRODUTO A SER COMPRADO CUSTA R${preco_Produto:,.2f} E O METODO
DE PAGAMENTO É À VISTA NO CARTAO.
E POR ISSO VOCÊ RECEBE UM DESCONTO DE 5%.
O NOVO PRECO A SER NECESSÁRIO É DE R${preco_NovoPreco:,.2f} ''')
    print('=' * 54)

elif decisao == 3:
    parcela = preco_Produto / 2
    preco_NovoPreco = parcela
    print(f'''O PRODUTO A SER COMPRADO CUSTA R${preco_Produto:,.2f} E O METODO
DE PAGAMENTO É 2x NO CARTAO.
SERÁ PRECISO PAGAR 2x PARCELAS DE R${parcela:,.2f}''')
    print('=' * 54)

elif decisao == 4:
    quant = int(input('DIGITE A QUANTIDADE DE PARCELAS:'))
    preco_NovoPreco = preco_Produto + (preco_Produto * 0.2)
    parcela = preco_NovoPreco / quant
    print(f'''O PRODUTO A SER COMPRADO CUSTA R${preco_Produto:,.2f} E O METODO
DE PAGAMENTO É 3x OU MAIS NO CARTAO.
POR ISSO SERÁ PRECISO PAGAR {quant} PARCELAS DE R${parcela:,.2f}
AO LONGO DE {quant} MESES COM JUROS DE 20%.
O VALOR FINAL SERÁ DE R${preco_NovoPreco:,.2f}.''')
    print('=' * 54)
