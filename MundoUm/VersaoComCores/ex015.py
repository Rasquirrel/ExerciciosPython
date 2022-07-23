# Progama desenvolvido por José Isac
# 22 de julho, 13:45
# Este progama irá perguntar a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele
# foi alugado. Após isso irá calcular o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print()
print('\033[1;33m-=' * 50)
print('DESAFIO N° 15')
print('\033[1;35mDesenvolva um aplicativo que irá calcular o preço a pagar por um carro alugado\n'
      'sabendo que um dia equivale a R$60,00 e R$0,15 por Km rodado.')
print('\033[1;33m-=' * 50)
print()

diasAlugado = int(input('\033[1;34mQuantos dias aluados? '))
kmPercorridos = float(input('\033[1;34mQuantos Km rodados? '))
precoAPagar = (60 * diasAlugado) + (0.15 * kmPercorridos)

print('\033[1;34mO total a pagar é de R$\033[1;33m{:.2f}'.format(precoAPagar))
