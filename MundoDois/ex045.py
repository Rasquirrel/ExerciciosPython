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

Option = ('Pedra', 'Papel', 'Tesoura')
comp_Option = Option[randint(0, 2)]

print('Vai!')
print('''[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')

player_Option = int(input())

sleep(1)
print('Pedra')
sleep(1)
print('Papel')
sleep(1)
print('Tesoura!')
print()

# Jogo
if comp_Option == 'Pedra':
	if player_Option == 0:
		print('Computador: PEDRA\nVocê: PEDRA\nEMPATE!')
	elif player_Option == 1:
		print('Computador: PEDRA\nVocê: PAPEL\nVOCÊ GANHOU!')
	elif player_Option == 2:
		print('Computador: PEDRA\nVocê: TESOURA\nCOMPUTADOR GANHOU!')
	else:
		print('Opção invalida!')

elif comp_Option == 'Papel':
	if player_Option == 0:
		print('Computador: PAPEL\nVocê: PEDRA\nCOMPUTADOR GANHOU!')
	elif player_Option == 1:
		print('Computador: PAPEL\nVocê: PAPEL\nEMPATE!')
	elif player_Option == 2:
		print('Computador: PAPEL\nVocê: TESOURA\nVOCÊ GANHOU!')
	else:
		print('Opção invalida!')

elif comp_Option == 'Tesoura':
	if player_Option == 0:
		print('Computador: TESOURA\nVocê: PEDRA\nVOCÊ GANHOU!')
	elif player_Option == 1:
		print('Computador: TESOURA\nVocê: PAPEL\nCOMPUTADOR GANHOU!')
	elif player_Option == 2:
		print('Computador: TESOURA\nVocê: TESOURA\nEMPATE')
	else:
		print('Opção inválida!')

