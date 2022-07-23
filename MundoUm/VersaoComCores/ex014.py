# Progama desenvolvido por José Isac
# 22 de julho, 13:34
# Converter teperatura de °C para °F

print()
print('\033[1;33m-=' * 50)
print('DESAFIO N° 15')
print('\033[1;35mDesenvolva um aplicativo que converta temperatura em °C para °F')
print('\033[1;33m-=' * 50)
print()

c = float(input('\033[1;34mInforme a temperatura em °C: '))
f = (9 * c) / 5 + 32
print('\033[1;34mA temperatura de \033[1;33m{}\033[1;34m°\033[1;35mC'
      '\033[1;34m corresponde a \033[1;33m{} °\033[1;31mF!'.format(c, f))
