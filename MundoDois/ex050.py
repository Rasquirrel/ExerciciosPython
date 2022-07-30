# Desenvolva um progama que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o

print('''Olá! Este progama irá ler o valor de seis números inteiros de sua preferência
e irá exibir apenas a soma daqueles que forem pares.''')

cont = 0
soma = 0

for c in range(1,7):
    numero = int(input(f'Digite {c} um número: '))
    if numero % 2 ==0:
        soma += numero
        cont += 1
print(f'Foi informado {cont} números pares e a soma de todos eles é {soma}.')
