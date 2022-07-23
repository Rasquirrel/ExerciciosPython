"""
Progama desenvolvido por José Isac
20 de julho, 6:47 PM

Este progama tem como função ler o nome de quatro alunos e sortear um deles para apagar o quadro
"""
from random import choice

aluno1 = input('Qual o nome do primeiro aluno? ')
aluno2 = input('Qual o nome do segundo aluno? ')
aluno3 = input('Qual o nome do terceiro aluno? ')
aluno4 = input('Qual o nome do quarto aluno? ')

print('O aluno sorteado é: ')
print(choice([aluno1, aluno2, aluno3, aluno4]))
