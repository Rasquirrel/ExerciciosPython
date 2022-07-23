# Progama desenvolvido por José Isac
# 23 de julho, 17:58

print()
print('\033[1;33m-=' * 50)
print('Desafio N° 30')
print('\033[35mDesenvolva um aplicativo que receba um número do usuário e informe a ele se é impar ou par.')
print('\033[1;33m-=' * 50)
print()

valor = float(input('\033[1;34mDigite um número: '))
if valor % 2 == 0:
    print('\033[32mO valor {} é par!'.format(valor))
else:
    print('\033[31mO valor {} é ímpar!'.format(valor))
