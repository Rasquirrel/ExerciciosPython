"""
Desenvolva um progama que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar
um triângulo.
"""
a = float(input('Qual o comprimento da reta A?'))
b = float(input('Qual o comprimento da reta B?'))
c = float(input('Qual o comprimento da reta C?'))

if a + b > c and a + c > b and b + c > a:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo.')
"""
if a == b == c:
    print('É possível formar um triângulo! Equilátero')
if a == b or b == c or c == a:
    print('É possível formar um triângulo! Isóceles')
if a != b != c:
    print('É possível formar um triângulo! Escaleno')
"""

"""
# Reta Maior:

if a > b and a > c:
    print('O maior número é: {}'.format(a))

if b > a and b > c:
    print('O maior número é: {}'.format(b))

if c > a and c > b:
    print('O maior número é: {}'.format(c))

# Reta Menor:

if a < b and a < c:
    menor = a
    print('O menor número é: {}'.format(menor))

if b < a and b < c:
    menor = b
    print('O menor número é: {}'.format(menor))

if c < a and c < b:
    menor = c
    print('O menor número é: {}'.format(menor))
"""