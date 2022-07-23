# faça um algoritmo que leia o salario de um funcionario, mas agora exiba o novo salário ele com 15% de aumento
salario = float(input('Digite o valor do seu atual salário: '))
salarioAumento = (salario * 15)/100
salarioNovo = salario + salarioAumento

print('Seu novo salário é: {}'.format(salarioNovo))
