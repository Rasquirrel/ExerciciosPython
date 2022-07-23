# Progama desenvolvido por José isac
# 23 de julho, 18:10

print()
print('\033[1;33m-=' * 50)
print('Desafio N°32')
print('\033[1;35mDesenvolva um progama que pergunte o salário de um funcionário e calcule o valor de seu aumento.'
      'Para salários superiores a R$1.250,00, calcule um aumento de 10%.Para os inferiores ou '
      'iguais, o aumento é de 15%.')
print('\033[1;33m-=' * 50, '\033[m')
print()

salario = float(input('\033[1;34mDigite o valor do seu salário: R$'))

if salario > 1250:
    aumento = (10/100) * salario
    novoSalario = salario + aumento
    print('Você recebeu um aumento de 10%. Seu salário passa de R${} para R${}.'.format(salario, novoSalario))
else:
    aumento = (15/100) * salario
    novoSalario = salario + aumento
    print('Você recebeu um aumento de 15%. Seu salário passa de R${} para R${}.'.format(salario, novoSalario))
