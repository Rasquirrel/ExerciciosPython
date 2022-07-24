"""
Progama desenvolvido por José Isac
24 de julho, 02:19PM
"""

# Dicionário de cores que eu utilizo para deixar os progamas com a aparência agradavel.

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
         'Close': '\033[m'}

# Cabeçalho

print('{}-='.format(cores['Roxa-N']) * 50, '\033[m')
print('{}DESAFIO N°37'.format(cores['Ciano-N']))
print('{}Desenvolva um progama que leia um número inteiro e peça para o usuário escolher qual será a base\n'
      'de conversão:\n'
      '1 - Para binário\n'
      '2 - Para octal\n'
      '3 - Para hexadecimal'.format(cores['Amarelo-N']))
print('{}-='.format(cores['Roxa-N']) * 50, '\033[m')

# Inicio

num = int(input('Digite um número: '))

print('_-' * 50)
print('Decida:\n'
      '1 - Converter para binário\n'
      '2 - Converter para octal\n'
      '3 - Converter para hexadecimal')
print('_-' * 50)

decisao = int(input())
if decisao == 1:
    print('{}'.format(bin(num)))
elif decisao == 2:
    print('{}'.format(oct(num)))
elif decisao == 3:
    print('{}'.format(hex(num)))
else:
    print('Opção Invalida :(')
