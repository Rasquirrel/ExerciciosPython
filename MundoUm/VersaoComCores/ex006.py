# Progama desenvolvido por José Isac
# 22 de julho, 11:25
# O objetivo desse progama é exibir o dobro, o tripo e a raiz quadrada de um número digitado pelo usuário.

from math import sqrt

print()
print('\033[1;33m-=' * 50)
print('DESAFIO N° 6\033[m')
print('\033[1;35mDesenvolver um progama que receba um número do usuário e após isso'
      ' exibir o dobro, \ntriplo e a raiz quadrada desse número.\033[m')
print('\033[1;33m-=' * 50, '\033[m')
print()

num = float(input('\033[1;34mDigite um número: '))
dobro = num * 2
triplo = num * 3
raiz = sqrt(num)

print('O dobro de \033[1;33m{} \033[1;34mvale \033[1;33m{}\033[1;34m.'.format(num, dobro))
print('O triplo de \033[1;33m{} \033[1;34mvale \033[1;33m{}\033[1;34m.'.format(num, triplo))
print('A raiz quadrada de \033[1;33m{} \033[1;34mé igual a \033[1;33m{}\033[1;34m.'.format(num, raiz))
