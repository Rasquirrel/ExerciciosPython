# Progama desenvolvido por José Isac
# 22 de julho, 15:16
# Este progama vai misturar a ordem dos elementos de uma lista

import random

print()
print('\033[1;33m-=' * 50)
print('DESAFIO N°19')
print('\033[1;35mDesenvolva um aplicativo que misture a ordem dos nomes de quatro alunos.')
print('\033[1;33m-=' * 50)
print()

nomeUm = str(input('\033[1;34mPrimeiro(a) aluno(a): '))
nomeDois = str(input('\033[1;34mSegundo(a) aluno(a): '))
nomeTres = str(input('\033[1;34mTerceiro(a) aluno(a): '))
nomeQuatro = str(input('\033[1;34mQuarto(a) aluno(a): '))

lista = [nomeUm, nomeDois, nomeTres, nomeQuatro]
random.shuffle(lista)

print('\033[1;34mA ordem escolhida será: \033[1;32m{}'.format(lista))
