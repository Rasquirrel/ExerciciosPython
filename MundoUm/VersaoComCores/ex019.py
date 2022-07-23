# Progama desenvolvido por José Isac
# 22 de julho, 15:06
# Este progama tem como objetivo sortear a escolha de um aluno dentre quatro

import random

print()
print('\033[1;33m-=' * 50)
print('DESAFIO N°19')
print('\033[1;35mDesenvolva um aplicativo que escolha um dentre quatro alunos.')
print('\033[1;33m-=' * 50)
print()

nomeUm = str(input('\033[1;34mPrimeiro(a) aluno(a): '))
nomeDois = str(input('\033[1;34mSegundo(a) aluno(a): '))
nomeTres = str(input('\033[1;34mTerceiro(a) aluno(a): '))
nomeQuatro = str(input('\033[1;34mQuarto(a) aluno(a): '))

lista = [nomeUm, nomeDois, nomeTres, nomeQuatro]
decisao = random.choice(lista)

print('\033[1;34mO aluno(a) escolhido(a) foi: \033[1;32m{}'.format(decisao))
