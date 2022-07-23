# Progama desenvolvido por José Isac
# 22 de julho, 13:07
# Este progama tem como objetivo calcular a área de uma parede e o quanto de tinta é necessário para pintar-la.

print()
print('\033[1;33m-=' * 50)
print('DESAFIO N° 11')
print('\033[1;35mDesenvolva um aplicativo que calcule a área de uma parede e calcule o quanto de tinta '
      'é necessário\npara pintar ela, sabendo que 1l pintam 2m²')
print('\033[1;33m-=' * 50)

largura = float(input('\033[1;34mLargura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de \033[1;33m{}\033[1;34mx\033[1;33m{}\033[1;34m'
      ' e sua área é de \033[1;33m{}\033[1;34mm².'.format(largura, altura, area))
print('Para pintar essa parede você precisará de \033[1;33m{}\033[1;34ml de tinta.'.format(tinta))
