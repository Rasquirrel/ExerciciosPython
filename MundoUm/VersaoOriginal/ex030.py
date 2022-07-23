"""
Crie um progama que leia um número inteiro e mostre na tela se ele é par ou ímpar
"""
print('Este progama irá lhe auxiliar em descobrir se um número é ímpar ou par.')

numero = int(input('Digite um número: '))
divisao = numero % 2

if divisao == 0:
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é ímpar!'.format(numero))
