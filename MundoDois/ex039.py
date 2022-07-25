# Progama desenvolvido por José Isac
# 25 de julho, 11:06

# Esta biblioteca será utilizada para sempre utilizar o ano atual como base de um cálculo
from datetime import date 

# Cabeçalho
print('-=' * 50)
print('DESAFIO N°39')
print('Desenvolva um progama que leia o ano de nascimento de um jovem e informe de acordo\n'
      'com sua idade:\n'
      '- Se ele ainda vai se alistar ao serviço militar;\n'
      '- Se ja é hora de se alistar;\n'
      '- Se já passou do tempo do alistamento;\n'
      'Seu progama também deverá mostrar o tempo que falta ou que passou do prazo.')
print('-=' * 50)
print()

# Início

ano_Nascimento = int(input('Digite o seu ano de nascimento: '))
ano_Atual = date.today().year
teste_Um = ano_Atual - ano_Nascimento
tempo_Faltando = 18 - teste_Um
tempo_Passou = teste_Um - 18

# Testes

if teste_Um < 18:
    print('Você ainda vai se alistar ao serviço militar. Você ainda possui {} anos até la.'.format(tempo_Faltando))
elif teste_Um > 18:
    print('Já passou da hora de se alistar! O prazo passou em {} anos.'.format(tempo_Passou))
elif teste_Um == 18:
    print('Já é hora de se alistar! Procure a Junta do Serviço Militar mais próxima.')
