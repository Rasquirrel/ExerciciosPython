# Progama desenvolvido por José Isac
# 23 de julho, 17:34

print()
print('\033[1;33m-=' * 50)
print('Desafio N° 27')
print('\033[1;35mDesenvolva um progama que realize um mini jogo da advinhação com o usuário.')
print('\033[1;33m-=' * 50, '\033[m')
print()

from random import randint

numero = randint(0, 5)
print('\033[1;34mO progama está pensando em um número de 0 a 5...')
print('Ele já decidiu qual é!')

advinha = int(input('Que número você acha que é? '))

if advinha == numero:
    print('Uau! Parabéns! Você ganhou! Até a próxima.')
else:
    print('Hihihi! Eu ganhei! O número era {}. Não foi dessa vez. Até a próxima'.format(numero))
