# Progama desenvolvido por José Isac
# 23 de julho, 17:48

print()
print('\033[1;33m-=' * 50)
print('Desafio n° 30')
print('\033[1;35mDesenvolva um aplicativo que leia a velocidade de um carro em Km/h.\n'
      'Se ele ultrapassar 80Km/h mostre uma mensagem dizendo que ele foi multado.\n'
      'A multa vai custar R$7,00 para cada Km acima do limite.')
print('\033[1;33m-=' * 50, '\033[m')
print()

valor = int(input('\033[1;34mOlá! Qual é a velocidade em Km/h do seu carro? '))

if valor > 80:
    velocAcimaDoLimite = valor - 80
    multa = float(velocAcimaDoLimite * 7)
    print('\033[34mATENÇÃO! Você está acima do limite de'
          ' velocidade por \033[1;31m{}Km/h.'.format(velocAcimaDoLimite))
    print('\033[34mVocê deverá pagar uma multa de R$\033[1;32m{:.2f}'.format(multa))
else:
    print('\033[1;34mTudo certo! Siga em frente e boa viagem!')
