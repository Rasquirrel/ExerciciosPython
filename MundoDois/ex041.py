# Progama desenvolvido por José Isac
# 26 de julho, 13:34
# Versão 1.0

# Biblioteca utilizada para deixar o progama um tiquinho mais dinâmico.
from datetime import date

# Cabeçalho

print('-=' * 50)
print('DESAFIO N°41')
print('''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta 
e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
''')
print('-=' * 50)

# Início

ano_Nascimento = int(input('Você nasceu em que ano? '))
ano_Atual = date.today().year
while ano_Nascimento >= ano_Atual:
    ano_Nascimento = int(input(
        f'Digite um ano de nascimento que não seja maior nem igual ao ano atual({ano_Atual}: )'))
idade = ano_Atual - ano_Nascimento

if 0 < idade < 9:
    print('ATLETA MIRIM')
elif 9 < idade < 14:
    print('ATLETA INFANTIL')
elif 14 < idade < 19:
    print('ATLETA JÚNIOR')
elif 19 < idade < 25:
    print('ATLETA SÊNIOR')
elif 25 < idade < 1000:
    print('ATLETA SÊNIOR')