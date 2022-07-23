"""
Faça um progama que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
Ex:
  Digite um número: 1834

  unidade: 4
  dezena : 3
  centena: 8
  milhar : 1

Progama desenvolvido por José Isac
21 de julho, em uma hora ai
"""

numero = int(input('Digite um número entre 0 a 9999: '))


unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print()
print('''\t\t unidade = {}\n
         dezena  = {}\n
         centena = {}\n
         milhar  = {}\n'''.format(unidade, dezena, centena, milhar))
