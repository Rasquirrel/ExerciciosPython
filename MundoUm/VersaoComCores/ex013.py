# Progama desenvolvido por José Isac
# 22 de julho, 13:27
# Este progama vai calcular o novo salário de um funcionário após um reajuste

print()
print('\033[1;33m-=' * 50)
print('DESAFIO N° 13')
print('\033[1;35mDesenvolva um aplicativo que calcule o novo valor do salário de um funcionário '
      'após um aumento de 15% ')
print('\033[1;33m-=' * 50)
print()

salario = float(input('\033[1;34mQual é o salário do Funcionário? R$'))
aumento = salario * (15/100)
novoSalario = salario + aumento

print('\033[1;34mUm funcionário que ganhava \033[1;32mR$\033[1;33m{}\033[1;34m, com 15% de aumento, passa a receber '
      '\033[1;32mR$\033[1;33m{:.2f}.'.format(salario, novoSalario))
