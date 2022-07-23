"""
Progama desenvolvido por José Isac
20 de julho, 6:35 PM

Este progama irá pedir um angulo qualquer e após isso irá exibir o valor do seno, cosseno e tangente
"""
from math import cos, sin, tan, radians

angulo = float(input('Digite o valor do angulo em graus :'))

anguloRad = radians(angulo)  # Precisa converter o angulo de graus para radianos

seno = sin(anguloRad)
cosseno = cos(anguloRad)
tangente = tan(anguloRad)

print('-' * 24)
print('Seu seno vale: {:.3f}\n Seu cosseno vale: {:.3f}\n Sua tangente vale: {:.3f}'.format(seno, cosseno, tangente))
print('-' * 24)
