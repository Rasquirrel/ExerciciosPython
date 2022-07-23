"""
Progama desenvolvido por José Isac
20 de julho, 6:24 PM

Este progama vai ler o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, calcular
e exibir o comprimento da hipotenusa
"""
from math import hypot

catetoOp = float(input('Qual o comprimento do cateto oposto? '))
catetoAdj = float(input('Qual o comprimento do cateto adjacente? '))

"""
hipotenusa = sqrt((pow(catetoOp, 2)+pow(catetoAdj, 2)))
"""

hipotenusa = hypot(catetoOp, catetoAdj)

print('O comprimento da hipotenusa é igual a: {:.2f}Uc'.format(hipotenusa))
