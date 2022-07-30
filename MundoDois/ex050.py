# Desenvolva um progama que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o

print('''Olá! Este progama irá ler o valor de seis números inteiros de sua preferência
e irá exibir apenas a soma daqueles que forem pares.''')

for c in range(1,7):
    numeroUm = int(input('Digite um número: '))
    numeroDois = int(input('Digite outro número: '))
    if numeroUm % 2 == 0 and numeroDois % 2 == 0:
        print(f'{numeroUm} + {numeroDois} = {numeroUm + numeroDois}')
    else:
        continue
