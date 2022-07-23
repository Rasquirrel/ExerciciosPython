# Progama desenvolvido por José Isac
# 22 de julho, 12:28
# O objetivo desse progama é converter USD em BRL. USD = R$5,44 EUR = R$5,54 YEN = R$0,04

print()
print('\033[1;33m-=' * 50)
print('DESAFIO N° 10')
print('\033[1;35mDesenvolver um aplicativo que ajude o usuário a descobrir a quantidade de USD, YEN e EUR \nque ele'
      ' pode comprar.')
print('\033[1;33m-=' * 50)
print()

reais = float(input('\033[1;34mQuanto dinheiro você tem na carteira? R$'))

usd = reais / 5.44
eur = reais / 5.54
yen = reais / 0.04

print('Com \033[1;34mR$\033[1;33m{:.2f} \033[1;34mvocê pode comprar US$\033[1;33m{:.2f}'.format(reais, usd))
print('\033[1;34mCom R$\033[1;33m{:.2f}\033[1;34m você pode comprar YEN\033[1;33m{:.2f}'.format(reais, yen))
print('\033[1;34mCom R$\033[1;33m{:.2f}\033[1;34m você pode comprar EUR$\033[1;33m{:.2f}'.format(reais, eur))
