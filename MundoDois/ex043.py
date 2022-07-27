# Progama desenvolvido por José Isac
# 27 de julho 8:40
# Versão 1.0
# Para calcular o IMC eu devo pegar o peso da pessoa em kg e dividir pela altura dela ao quadrado

print('-=' * 50)
print('DESAFIO N°43')
print('''Desenvolva um aplicativo que ajude o usuário a calcular o IMC.
Se o IMC for abaixo de 18,5 - Abaixo do peso
Se o IMC for entre 18,5 e 25 - Peso ideal
Se o IMC for entre 30 e 40 - Obesidade
Se o IMC for acima de 40 - Obesidade Mórbida''')
print('-=' * 50)

peso = float(int('Informe seu peso em Kg: '))
altura = float(int('Informe sua altura: '))
imc = peso / altura**2

if 18.5 > imc:
    print('Você pesa {}Kg e possui o IMC de {}, o que significa que você tem:')
    print('ABAIXO DO PESO')
elif 18.5 < imc < 25:
    print('Você pesa {}Kg e possui o IMC de {}, o que significa que você tem:')
    print('PESO IDEAL')
elif 30 < imc < 40:
    print('Você pesa {}Kg e possui o IMC de {}, o que significa que você tem:')
    print('OBESIDADE')
elif 40 < imc:
    print('Você pesa {}Kg e possui o IMC de {}, o que significa que você tem:')
    print('OBESIDADE MÓRBIDA')
