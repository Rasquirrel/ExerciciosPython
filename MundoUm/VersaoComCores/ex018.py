# Este progama foi desenvolvido por José Isac
# 22 de julho, 14:56
# Este progama tem como objetivo calcular o seno, cosseno e tangente de um angulo qualquer

from math import radians, sin, cos, tan

print()
print('\033[1;33m-=' * 50)
print('DESAFIO N° 18')
print('\033[1;35mDesenvolva um progama que calcule o seno, cosseno e tangente de um ângulo qualquer.')
print('\033[1;33m-=' * 50)
print()

angulo = float(input('\033[1;34mDigite o ângulo que você deseja: '))
radianos = radians(angulo)
sen = sin(radianos)
cosen = cos(radianos)
tang = tan(radianos)

print('O ângulo de \033[1;33m{}°\033[1;34m tem o SENO de \033[1;33m{:.1f}\033[1;34m.'.format(angulo, sen))
print('O ângulo de \033[1;33m{}°\033[1;34m tem o COSSENO de \033[1;33m{:.1f}\033[1;34m.'.format(angulo, cosen))
print('O ângulo de \033[1;33m{}° \033[1;34mtem a TANGENTE de \033[1;33m{:.1f}\033[1;34m.'.format(angulo, tang))
