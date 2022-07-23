# Progama desenvolvido por José Isac
# 22 de julho, 13:19
# Este progama vai calcular o desconto de um produto e exibir o seu novo preço

print()
print('\033[1;33m-=' * 50)
print('DESAFIO N° 12')
print('\033[1;35mDesenvolva um aplicativo que pergunte ao usuário o preço de um produto,'
      'aplique\n5% de desconto e exiba o novo preço.')
print('\033[1;33m-=' * 50)

preco = float(input('\033[1;34mQual é o preço do produto? \033[1;32mR$'))
desconto = preco * (5/100)
novoPreco = preco - desconto

print('\033[1;34mO produto que custava \033[1;32mR$\033[1;33m{},'
      ' \033[1;34mna promoção com desconto de 5% '
      'vai custar \033[1;32mR$\033[1;33m{:.2f}\033[1;34m.'.format(preco, novoPreco))
