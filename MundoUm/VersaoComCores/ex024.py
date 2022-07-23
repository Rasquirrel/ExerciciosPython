# Progama desenvolvido por José Isac
# 23 de julho, 17:06
# Este progama tem como objetivo ler o nome de uma cidade e analisar se começa com 'Santo'

print()
print('\033[1;33m-=' * 50)
print('Desafio N° 24')
print('\033[1;35mDesenvolva um aplicativo que leia o nome de uma cidade e identifique se ela começa com \"Santo\".')
print('\033[1;33m-=' * 50, '\033[m')
print()

cidade = str(input('\033[1;34mDigite o nome da cidade: '))
cidadeDividida = cidade.upper().strip().split()
print('A sua cidade começa com Santo? \033[1;31m', 'SANTO' in cidadeDividida)
