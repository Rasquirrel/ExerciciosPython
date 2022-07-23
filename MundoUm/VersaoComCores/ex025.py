# Progama desenvolvido por José Isac
# 23 de julho, 17:18
# Este progama tem como objetivo descobrir se eu tenho 'Silva' no nome

print()
print('\033[1;33m-=' * 50)
print('Desafio N° 25')
print('\033[1;35mDesenvolva um aplicativo que ajude o usuário a descobrir se ele possui Silva no nome.')
print('\033[1;33m-=' * 50, '\033[m')
print()

nome = str(input('\033[1;34mDigite o seu nome: '))
print('\033[1;34mVocê possui \"Silva\" no nome? \033[1;31m{}'.format('SILVA' in (nome.upper().strip())))
