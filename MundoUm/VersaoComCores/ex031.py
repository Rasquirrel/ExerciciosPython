# Progama desenvolvido por José Isac
# 23 de julho, 18:02

print()
print('\033[1;33m-=' * 50)
print('Desafio N° 31')
print('\033[35mDesenvolva um progama que pergunte a distância de uma viagem em Km. Calcule o preço da passagem '
      'cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas')
print('\033[1;33m-=' * 50)
print()

distancia = int(input('\033[1;34mQual a distância em Km, da sua viagem? '))

if distancia > 200:
    preco = distancia * 0.45
    print('\033[1;34mSerá preciso pagar {}R$ por essa viagem.'.format(preco))
else:
    preco = distancia * 0.50
    print('\033[1;34mSerá preciso pagar {}R$ por essa viagem.'.format(preco))
