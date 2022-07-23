# Progama desenvolvido por José isac
# 23 de julho, 18:08

print()
print('\033[1;33m-=' * 50)
print('Desafio N°32')
print('\033[1;35mDesenvolva um aplicativo que leia três números e informe qual o maior e qual o menor.')
print('\033[1;33m-=' * 50, '\033[m')
print()

num1 = int(input('\033[1;34mDigite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o primeiro número: '))


# MANEIRA COMPLETA

if num1 > num2 and num1 > num3:
    print('O maior número é: {}'.format(num1))

if num2 > num1 and num2 > num3:
    print('O maior número é: {}'.format(num2))

if num3 > num1 and num3 > num2:
    print('O maior número é: {}'.format(num3))

if num1 < num2 and num1 < num3:
    print('O menor número é: {}'.format(num1))

if num2 < num1 and num2 < num3:
    print('O menor número é: {}'.format(num2))

if num3 < num1 and num3 < num2:
    print('O menor número é: {}'.format(num3))
