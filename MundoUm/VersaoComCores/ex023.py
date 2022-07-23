# Progama desenvolvido por José Isac
# 23 de julho, 16:54
# O objetivo deste progama é exibir separadamente cada digito de um número de quatro digitos.

print()
print('\033[1;33m-=' * 50)
print('Desafio N° 23')
print('\033[1;35mDesenvolva um aplicativo que leia um número de 0 a 9999 e exiba na tela cada digito\n'
      'separado.')
print('\033[1;33m-=' * 50, '\033[m')
print()

num = int(input('\033[1;34mDigite um número: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print('\033[1;34mUnidade = \033[1;36m{}\033[m'.format(unidade))
print('\033[1;34mDezena = \033[1;36m{}\033[m'.format(dezena))
print('\033[1;34mCentena = \033[1;36m{}\033[m'.format(centena))
print('\033[1;34mMilhar = \033[1;36m{}\033[m'.format(milhar))
