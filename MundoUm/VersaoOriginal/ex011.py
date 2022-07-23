# Crie um progama que leia a altura e a largura de uma parede em metros, calcule sua area e a quantidade de tinta
# necessária para pintar-la sabendo que cada litro pinta 2m²

altura = float(input('Qual é a altura da parede em metros?'))
largura = float(input('Qual é a largura da parede em metros?'))
area = altura * largura
quantidadeTinta = area / 2

print('A quantidade de tinta necessária para pintar essa parede é {}'.format(quantidadeTinta))
