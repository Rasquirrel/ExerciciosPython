# Progama desenvolvido por José Isac
# 23 de julho, 17:34

print()
print('\033[1;33m-=' * 50)
print('Desafio N° 27')
print('\033[1;35mDesenvolva um '
      'progama que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o último nome separadamente.')
print('\033[1;33m-=' * 50, '\033[m')
print()

nome = input('\033[1;34mDigite o seu nome completo: ').strip().split()

print('Seu primeiro nome é: \033[1;33m', nome[0])
print('\033[1;34mSeu ultimo nome é: \033[1;33m', nome[-1])
