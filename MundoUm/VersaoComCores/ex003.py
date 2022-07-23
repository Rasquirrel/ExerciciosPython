# Progama desenvolvido por José Isac
# 22 de julho, 10:32
# O objetivo deste progama é receber dois números do usuário e somar eles

print()
print('\033[1;33m-=' * 50)
print('DESAFIO N° 3')
print('\033[1;35mDesenvolver um progama que receba dois números do usuário, some eles e exiba o resultado.\033[m')
print('\033[1;33m-=' * 50, '\033[m')

num1 = int(input('\033[1;34mDigite um valor: \033[m'))
num2 = int(input('\033[1;34mDigite outro valor: \033[m'))

soma = num1 + num2

print('\033[1;34mA soma entre \033[1;33m{}\033[m \033[1;34me \033[1;33m{}\033[m \033[1;34mé igual a \033[1;33m{}\033['
      'm!\033[m'.format(num1, num2, soma))
