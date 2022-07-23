"""
Crie um progama que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

Progama desenvolvido por José Isac
Em 21 de julho, 1:49 PM
"""
nome = input('Qual o seu nome? ').strip().upper()
print('Seu nome possui \"Silva\"? ', 'SILVA' in nome)
