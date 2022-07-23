"""
Crie um progama que leia o nome de uma cidade e dizer se a cidade começa ou não com o nome "Santo"
Progama desenvolvido por José Isac
21 de julho, 1:47 PM
"""
cidade = input('Qual o nome da cidade? ').strip().upper()

cidadeDividida = cidade.split()

print('A sua cidade começa com \"Santo\"? ', 'SANTO' in cidadeDividida[0])
