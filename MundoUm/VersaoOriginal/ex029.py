"""
Escreva um progama que leia a velocidade de um carro em km/h. Se ele ultrapassar 80km/h, mostre
uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 para cada Km acima do limite.
"""
print('Qual a velocidade do seu carro em Km/h no momento? ')
velocidade = int(input(''))

if velocidade > 80:
    velocAcimaDolimite = velocidade - 80
    multa = float(velocAcimaDolimite * 7)
    print('Sua velocidade está acima do limite de 80Km/h! Você foi multado em R${:.2f}.'.format(multa))
else:
    print('Você pode relaxar e continuar sua viagem! Está tudo certo.')
