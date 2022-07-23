# Progama desenvolvido por José Isac
# 22 de julho, 10:22
# O objetivo deste progama é receber o nome de uma pessoa e exibir uma mensagem de boas vindas

print()
print('\033[1;33m-=' * 50)
print('DESAFIO N° 2\033[m')
print('\033[1;35mDesenvolver um progama que receba o nome de uma pessoa e exiba uma mensagem de boas vindas.\033[m')
print('\033[1;33m-=' * 50, '\033[m')

nome = str(input('\033[1;34mDigite seu nome: \033[m'))

print('É um \033[1;36mprazer\033[m te conhecer, \033[1;33m{}\033[m!'.format(nome))
