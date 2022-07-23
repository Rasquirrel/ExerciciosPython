# Progama desenvolvido por José Isac
# 22 de julho,  14:37
# Este progama tem como objetivo definir o tamanho da hipotenusa de acordo com o tamanho dos catetos

from math import hypot

print()
print('\033[1;33m-=' * 50)
print('DESAFIO N° 17')
print('\033[1;35mDesenvolva um aplicativo que calcule o tamanho da hipotenusa de acordo com o tamanho\n'
      'dos catetos.')
print('\033[1;33m-=' * 50)
print()

oposto = float(input('\033[1;34mComprimento do cateto oposto: '))
adjacente = float(input('\033[1;34mComprimento do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print('\033[1;34mA hipotenusa vai medir \033[1;33m{:.2f}.'.format(hipotenusa))
