# Progama desenvolvido por José Isac
# 22 de julho, 10:48
# O objetivo desse progama é pedir para que o usuário digite
# algo e após isso exibir todas as informações possíveis sobre aquilo

print()
print('\033[1;33m-=' * 50)
print(' DESAFIO N° 4')
print('\033[1;35m Desenvolver um progama que leia algo digitado pelo teclado e\n '
      'exibir seu tipo primitivo e todas as informações '
      'possíveis sobre ele.\033[m')
print('\033[1;33m-=' * 50, '\033[m')

print()
algo = str(input('\033[1;34mDigite algo: '))

print('\033[1;34mO tipo primitivo desse valor é:\033[m \033[1;33m{}\033[m'.format(type(algo)))
print('\033[1;34mSó tem espaços?\033[m \033[1;33m{}\033[m'.format(algo.isspace()))
print('\033[1;34mÉ um número?\033[m \033[1;33m{}\033[m'.format(algo.isnumeric()))
print('\033[1;34mÉ alfabético?\033[m \033[1;33m{}\033[m'.format(algo.isalpha()))
print('\033[1;34mÉ alfanumérico?\033[m \033[1;33m{}\033[m'.format(algo.isalnum()))
print('\033[1;34mEstá em maiúsculas?\033[m \033[1;33m{}\033[m'.format(algo.isupper()))
print('\033[1;34mEstá em minúsculas?\033[m \033[1;33m{}\033[m'.format(algo.islower()))
print('\033[1;34mEstá capitalizada?\033[m \033[1;33m{}\033[m'.format(algo.istitle()))
