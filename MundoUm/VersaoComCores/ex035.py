# Progama desenvolvido por José isac
# 23 de julho, 18:11

print()
print('\033[1;33m-=' * 50)
print('Desafio N°32')
print('\033[1;35mDesenvolva um progama que leia o comprimento de três retas e diga '
      'ao usuário se elas podem ou não formar um triângulo.')
print('\033[1;33m-=' * 50, '\033[m')
print()

a = float(input('Qual o comprimento da reta A?'))
b = float(input('Qual o comprimento da reta B?'))
c = float(input('Qual o comprimento da reta C?'))

if a + b > c and a + c > b and b + c > a:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo.')
