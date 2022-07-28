# Progama desenvolvido por José Isac
# 28 de julho, 11:40
# Pedra papel tesoura

# É um dos primeiros progamas em python que eu desenvolvo enquanto aprendo
# a utilizar o editor de textos para terminal, VIM.

from random import randint
from time import sleep

print('-=' * 40)
print('DESAFIO N°45')
print('Desenvolva o jogo Jokenpo')
print('-=' * 40)
print()

print('BEM VINDO AO JOGO DE PEDRA PAPEL TESOURA!')
print('Vamos jogar!')

comp_Option = randint(0, 2)

print('Vai!')
print('''[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')

player_Option = int(input())

print('Pedra')
sleep(1.9)
print('Papel')
sleep(1)
print('Tesoura!')
print()

if player_Option == 0 and comp_Option == 0:
	print('Computador: PEDRA')
	print('Você: PEDRA')
	print('Empate! Até a próxima!')
elif player_Option == 0 and comp_Option == 1:
	print('Computador: PAPEL')
	print('Você: PEDRA')
	print('Você perdeu! Até a próxima!')
elif player_Option == 0 and comp_Option == 2:
	print('Computador: TESOURA')
	print('Você: PEDRA')
	print('Você ganhou! Até a próxima!')

# Caso o jogador escolha tesoura

if player_Option == 2 and comp_Option == 0:
	print('Computador: PEDRA')
	print('Você: TESOURA')
	print('Você perdeu, até a próxima!')
elif player_Option == 2 and comp_Option == 1:
	print('Computador: TESOURA')
	print('Você: TESOURA')
	print('Empate! Até a próxima!')
elif player_Option == 2 and comp_Option == 2:
	print('Computador: PAPEL')
	print('Você: TESOURA')
	print('Você ganhou! Até a próxima!')

# Caso o jogador escolha papel
if player_Option == 1 and comp_Option == 0:
	print('Computador: PEDRA')
	print('Você: PAPEL')
	print('Você ganhou! Até a próxima!')
elif player_Option == 1 and comp_Option == 2:
	print('Computador: TESOURA')
	print('Você: PAPEL')
	print('Você perdeu! Até a próxima!')
elif player_Option == 1 and comp_Option == 1:
	print('Computador: PAPEL')
	print('Você: PAPEL')
	print('Empate! Até a próxima!')

