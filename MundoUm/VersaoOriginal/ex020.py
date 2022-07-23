"""
Progama desenvolvido por José Isac
20 de julho, 7:03 PM

Este progama vai sortear a ordem de apresentação de trabalho de 4 alunos e exibir o nome dos alunos na ordem decidida.
"""
from random import shuffle

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
print('A nova ordem de apresentação será: ')
shuffle(lista)
print(lista)
