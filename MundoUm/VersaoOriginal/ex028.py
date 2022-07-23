"""
Escreva um progama que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
para o usuário tentar descobrir qual foi o número escolhido pelo computador. O computador
deverá escrever na tela se o usuário venceu ou perdeu.

Progama desenvolvido por José Isac
21 de julho, 4:12 PM
"""
from random import randint

numero = randint(0, 5)
print('O progama está pensando em um número de 0 a 5...')
print('Ele já decidiu qual é!')

advinha = int(input('Que número você acha que é? '))

if advinha == numero:
    print('Uau! Parabéns! Você ganhou! Até a próxima.')
else:
    print('Hihihi! Eu ganhei! O número era {}. Não foi dessa vez. Até a próxima'.format(numero))
