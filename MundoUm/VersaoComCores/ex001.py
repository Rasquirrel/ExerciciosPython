# Progama desenvolvido por José Isac
# 22 de julho, 09:58
# O objetivo deste progama é exibir "olá mundo"

msg = 'Olá Mundo!'
cores = {'azul': '\033[34m',
         'amarelo': '\033[33m',
         'ciano': '\033[36m',
         'cinza': '\033[37m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',
         'magenta': '\033[35m',
         'limpo': '\033[m'}

estilos = {'bold': '\033[1'}

print()
print('\033[1;33m-='*40)
print('DESAFIO N° 1\033[m')
print('\033[1;35mDesenvolver um progama que exiba \"Olá Mundo!\" \033[m')
print('\033[1;33m-='*40)

print('{}{}{}'.format(cores['azul'], msg, cores['limpo']))
