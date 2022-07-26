# Progama desenvolvido por José Isac
# 26 de julho, 13:18
# Versão 1.2

# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média
# Dicionario de cores que eu utilizo para deixar os progamas bonitos
cores = {'Roxa-N': '\033[1;35m',
         'Roxa': '\033[35m',
         'Ciano': '\033[36m',
         'Ciano-N': '\033[1;36m',
         'Azul-N': '\033[1;34m',
         'Azul': '\033[34m',
         'Verde': '\033[32m',
         'Verde-N': '\033[1;32m',
         'Amarelo': '\033[33m',
         'Amarelo-N': '\033[1;33m',
         'Vermelho': '\033[31m',
         'Vermelho-N': '\033[1;31m',
         'Branco-N': '\033[1;30m',
         'Branco': '\033[30m',
         'Close': '\033[m'}

print('{}-='.format(cores['Roxa-N']) * 50, '\033[m')
print('{}DESAFIO N°40'.format(cores['Ciano-N']))
print('{}Crie um progama que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem\n'
      'no final de acordo com a média atingida. Média abaixo de 5 é reprovado, entre 5 e 6.9 é rec\n'
      'uperação, média 7 ou superior é aprovado.'.format(cores['Amarelo-N']))
print('{}-='.format(cores['Roxa-N']) * 50, '\033[m')
print()

# Inicio

print('''{}Bem vindo ao progama do cálculo de média!
Irei pedir dois valores de nota.
Se a média delas for abaixo de 5, retornarei {}REPROVADO;
{}Se a média delas for entre 5 e 6.9, retornarei {}RECUPERAÇÃO;
{}Se a média delas for 7 ou superior, retornarei {}APROVADO.
'''.format(cores['Azul-N'], cores['Vermelho-N'], cores['Azul-N'], cores['Amarelo-N'], cores['Azul-N'], cores['Verde-N']))

# Prompts

nota_Um = float(input('{}DIGITE O VALOR DA PRIMEIRA NOTA: '.format(cores['Azul-N'])))
while nota_Um > 10 or nota_Um < 0:
    print('POR FAVOR, INSIRA UM VALOR ENTRE 0 E 10.')
    nota_Um = float(input('DIGITE O VALOR DA PRIMEIRA NOTA: '))

nota_Dois = float(input('DIGITE O VALOR DA SEGUNDA NOTA: '))
while nota_Dois > 10 or nota_Dois < 0:
    print('POR FAVOR, INSIRA UM VALOR ENTRE 0 E 10.')
    nota_Dois = float(input('DIGITE O VALOR DA SEGUNDA NOTA: '))

# Calculo da média

media = (nota_Um + nota_Dois) / 2

# Testes

if media >= 7:
    print(f'SUA MÉDIA É {media:.1f} E VOCÊ ESTÁ APROVADO! PARABENS')
elif 5 < media < 6.9:
    print(f'SUA MÉDIA É {media:.1f} E VOCÊ ESTÁ DE RECUPERAÇÃO! BOA SORTE')
elif media < 5:
    print(f'SUA MÉDIA É {media:.1f} E VOCÊ ESTÁ REPROVADO! ATÉ A PRÓXIMA!')
