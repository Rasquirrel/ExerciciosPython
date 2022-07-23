# Progama desenvolvido por José Isac
# 22 de julho, 11:45
# Este progama tem como objetivo receber do usuário uma medida em metros, converter
# para Km, Hm, Dam, Dm, Cm, Mm e exibir na tela.

"""
Irei utilizar essa função trunc() da biblioteca math para remover com facilidade o ponto flutuante
de alguns valores mais abaixo.
"""

from math import trunc

print()
print('\033[1;33m-=' * 50)
print('DESAFIO N° 8')
print('\033[1;35mDesenvolver um progama que converta uma medida em metros para Km, Hm, Dam,\nCm e Mm.')
print('\033[1;33m-=' * 50, '\033[m')
print()

medida = float(input('\033[1;34mUma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = trunc(medida * 10)
cm = trunc(medida * 100)
mm = trunc(medida * 1000)

print('A medida de \033[1;33m{}m\033[1;34m corresponde a: '.format(medida))
print('\033[1;33m{}\033[1;31mKm'.format(km))
print('\033[1;33m{}\033[1;32mHm'.format(hm))
print('\033[1;33m{}\033[1;33mDam'.format(dam))
print('\033[1;33m{}\033[1;34mDm'.format(dm))
print('\033[1;33m{}\033[1;35mCm'.format(cm))
print('\033[1;33m{}\033[1;36mMm'.format(mm))
