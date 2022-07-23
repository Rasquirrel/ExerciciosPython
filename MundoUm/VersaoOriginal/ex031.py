"""
Desenvolva um progama que pergunte a distância de uma viagem em Km. Calcule o preço da passagem
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
"""

distancia = int(input('Qual a distância em Km, da sua viagem? '))

if distancia > 200:
    preco = distancia * 0.45
    print('Será preciso pagar {}R$ por essa viagem.'.format(preco))
else:
    preco = distancia * 0.50
    print('Será preciso pagar {}R$ por essa viagem.'.format(preco))
