# Progama desenvolvido por José Isac
# 22 de julho, 11:37
# Este progama tem como objetivo calcular a média de duas notas.

print()
print('\033[1;33m-=' * 50)
print('DESAFIO N° 7')
print('\033[1;35mDesenvolver um progama que irá receber duas '
      'notas do usuário, calcular e exibir a média delas.')
print('\033[1;33m-=' * 50, '\033[m')
print()

notaUm = float(input('\033[1;34mPrimeira nota do aluno: '))
notaDois = float(input('Segunda nota do aluno: '))
media = (notaUm + notaDois) / 2

print('A média entre \033[1;33m{}\033[1;34m e\033[1;33m {}\033[1;34m '
      'é igual a\033[1;33m {}\033[1;34m.'.format(notaUm, notaDois, media))
