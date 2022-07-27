# Progama desenvolvido por José Isac
# 27 de julho, 8:08
# Versão 1.0
# Para mim saber se três retas formam um triângulo, a soma de dois lados tem que ser maior que o terceiro lado.

print('-=' * 50)
print('DESAFIO N°42')
print('''Desenvola um aplicativo que ajude o usuário a descobrir se três retas
formam um triângulo e após isso informe qual o tipo de triângulo.
''')
print('-=' * 50)

reta_A = float(input('Digite o valor da primeira reta: '))
reta_B = float(input('Digite o valor da segunda reta: '))
reta_C = float(input('Digite o valor da terceira reta: '))

if reta_A + reta_B > reta_C and reta_B + reta_C > reta_A and reta_C + reta_A > reta_B:
    if reta_A == reta_B == reta_C:
        print('É POSSÍVEL FORMAR UM TRIÂNGULO EQUILÁTERO')
    elif (reta_A == reta_B) and (reta_A == reta_B) < reta_C:
        print('É POSSÍVEL FORMAR UM TRIÂNGULO ISÓCELES')
    else:
        print('É POSSÍVEL FORMAR UM TRIÂNGULO ESCALENO')
else:
    print('NÃO SERÁ POSSÍVEL FORMAR UM TRIÂNGULO')
