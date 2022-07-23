"""
Progama desenvolvido por José Isac
20 de julho, 6:09 PM

Este progama tem como função ler um número real qualquer e mostrar na tela sua porção inteira
"""
import math

num = float(input('Digite um número: '))
porcaoInteira = math.trunc(num)

print('A parte inteira de {} é {}'.format(num, porcaoInteira))
