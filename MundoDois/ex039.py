# Progama desenvolvido por José Isac
# Update 1.5, 25 de julho, 12:13

# Esta biblioteca será utilizada para sempre utilizar o ano atual como base de um cálculo
from datetime import date 

# Dicionário de cores que eu utilizo para deixar os progamas mais agradáveis
cores = {'Roxa-N': '\033[1;35m',
         'Roxa': '\033[35m',
         'Ciano': '\033[36m',
         'Ciano-N': '\033[1;36m',
         'Azul-N': '\033[1;34m',
         'Azul': '\033[34m',
         'Verde': '\033[32m',
         'Verde-N': '\033[1;32m',
         'Amarelo': '\033[33m',
         'Amarelo-N': '\033[1;33m',
         'Vermelho': '\033[31m',
         'Vermelho-N': '\033[1;31m',
         'Branco-N': '\033[1;30m',
         'Branco': '\033[30m',
         'Close': '\033[m'}


# Cabeçalho
print('{}-='.format(cores['Roxa-N']) * 50, '\033[m')
print('{}DESAFIO N°39{}'.format(cores['Ciano-N'], cores['Close']))
print('{}Desenvolva um progama que leia o ano de nascimento de um jovem e informe de acordo\n'
      'com sua idade:\n'
      '- Se ele ainda vai se alistar ao serviço militar;\n'
      '- Se ja é hora de se alistar;\n'
      '- Se já passou do tempo do alistamento;\n'
      'Seu progama também deverá mostrar o tempo que falta ou que passou do prazo.'.format(cores['Amarelo-N']))
print('{}-='.format(cores['Roxa-N']) * 50, '\033[m')
print()

# Início

ano_Nascimento = int(input('{}Digite o seu ano de nascimento: '.format(cores['Azul-N'])))
ano_Atual = date.today().year
idade = ano_Atual - ano_Nascimento
tempo_Faltando = 18 - idade
tempo_Passou = idade - 18
ano_Alistamento = ano_Atual + tempo_Faltando
ano_APassou = ano_Atual - tempo_Passou

# Testes

if idade < 18:
    print('{}Você nasceu em {} e possui {} anos.'.format(cores['Azul-N'], ano_Nascimento, idade))
    print('{}Você ainda vai se alistar ao serviço militar daqui a {}{}{}2006 anos em {}.'
    ''.format(cores['Verde-N'], cores['Vermelho-N'], tempo_Faltando, cores['Verde-N'], ano_Alistamento))
elif idade > 18:
    print('{}Você nasceu em {} e possui {} anos.'.format(cores['Azul-N'], ano_Nascimento, idade))
    print('{}Já passou da hora de se alistar! ' 
    'Você deveria ter se alistado a {}{} atrás em {}.'.format(cores['Vermelho-N'], tempo_Passou, cores['Vermelho-N'], ano_APassou ))
elif idade == 18:
    print('{}Você nasceu em {} e possui {} anos.'.format(cores['Azul-N'], ano_Nascimento, idade))
    print('{}Já é hora de se alistar! Procure a Junta do Serviço Militar mais próxima.'.format(cores['Roxa-N']))
