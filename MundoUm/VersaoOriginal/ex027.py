"""
Faça um progama que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o último nome separadamente.
Progama Desenvolvido por José Isac
21 de julho,  2:11 PM
"""

nome = input('Digite o seu nome completo: ').strip().split()

print('Seu primeiro nome é: ', nome[0])
print('Seu ultimo nome é: ', nome[-1])
