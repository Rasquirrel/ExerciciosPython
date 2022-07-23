# Progama desenvolvido por José Isac
# 22 de julho, 13:51
# Este progama tem como objetivo receber um número real e dizer sua parte inteira

from math import trunc

print()
print('\033[1;33m-=' * 50)
print('DESAFIO N° 16')
print('\033[1;35mDesenvolver um progama que leia um número real e informe sua parte inteira.')
print('\033[1;33m-=' * 50)
print()

valor = float(input('\033[1;34mDigite um valor: '))
print('O valor digitado foi \033[1;33m{}\033[1;34m e a sua porção inteira é: \033[1;33m{}'.format(valor, (trunc(valor))))
