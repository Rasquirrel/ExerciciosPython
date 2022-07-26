# Progama desenvolvido por José Isac
# 26 de julho, 11:29
# Versão 1.0

# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida
print('-=' * 50)
print('DESAFIO N°40')
print('Crie um progama que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem\n'
      'no final de acordo com a média atingida. Média abaixo de 5 é reprovado, entre 5 e 6.9 é rec\n'
      'uperação, média 7 ou superior é aprovado.')
print('-=' * 50)
print()

# Inicio

print('''Bem vindo ao progama do cálculo de média!
Irei pedir dois valores de nota.
Se a média delas for abaixo de 5, retornarei REPROVADO;
Se a média delas for entre 5 e 6.9, retornarei RECUPERAÇÃO;
Se a média delas for 7 ou superior, retornarei APROVADO.
''')

# Prompts

nota_Um = float(input('DIGITE O VALOR DA PRIMEIRA NOTA: '))
nota_Dois = float(input('DIGITE O VALOR DA SEGUNDA NOTA: '))

# Calculo da média

media = (nota_Um + nota_Dois) / 2

# Testes

if media >= 7:
    print(f'SUA MÉDIA É {media} E VOCÊ ESTÁ APROVADO! PARABENS')
elif 5 < media < 6.9:
    print(f'SUA MÉDIA É {media} E VOCÊ ESTÁ DE RECUPERAÇÃO! BOA SORTE')
elif media < 5:
    print(f'SUA MÉDIA É {media} E VOCÊ ESTÁ REPROVADO! ATÉ A PRÓXIMA!')
