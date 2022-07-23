# Progama desenvolvido por José isac
# 23 de julho, 18:05

print()
print('\033[1;33m-=' * 50)
print('Desafio N°32')
print('\033[1;35mDesenvolva um aplicativo que leia um ano qualquer e informe se ele é um ano bissexto.')
print('\033[1;33m-=' * 50, '\033[m')
print()

ano = int(input('\033[1;34mDigite um ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[1;34mO ano {} é bissexto!'.format(ano))
else:
    print('\033[1;34mO ano {} não é bissexto!'.format(ano))
