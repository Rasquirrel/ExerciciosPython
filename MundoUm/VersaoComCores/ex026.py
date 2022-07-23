# Progama desenvolvido por José Isac
# 23 de julho, 17:24

print()
print('\033[1;33m-=' * 50)
print('Desafio N° 26')
print('\033[1;35mDesenvolva um aplicativo que leia uma frase e informe quantas vezes a letra A aparece, sua\n'
      'primeira vez e ultima vez que aparece.')
print('\033[1;33m-=' * 50, '\033[m')
print()

frase = str(input('\033[1;34mDigite a frase: ')).strip().upper()
numA = frase.count('A')
primA = frase.find('A')
ultmA = frase.rfind('A')

print('\033[1;34mA letra \033[1;32mA\033[1;34m aparece \033[1;36m{}\033[1;34m vezes na frase.'.format(numA))
print('\033[1;34mA letra \033[1;32mA\033[1;34m aparece pela primeira vez na posição \033[1;36m{}.'.format(primA + 1))
print('\033[1;34mA letra \033[1;32mA\033[1;34m aparece pela última vez na posição \033[1;36m{}.'.format(ultmA + 1))
