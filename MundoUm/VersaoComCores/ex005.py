# Progama desenvolvido por José Isac
# 22 de julho, 11:11
# Este progama vai pedir um número ao usuário e depois irá exibir o antecessor e sucessor

print()
print('\033[1;33m-=' * 50)
print('DESAFIO N° 5\033[m')
print('\033[1;35mDesenvolver um progama que exiba o antecessor e o sucessor de um número digitado pelo usuário.\033[m')
print('\033[1;33m-=' * 50, '\033[m')
print()

num = int(input('\033[1;34mDigite um número: \033[m'))
antecessor = num - 1
sucessor = num + 1

print('\033[1;34mAnalisando o valor \033[1;33m{}, \033[1;34mseu antecessor é \033[1;33m{} \033[1;34me o sucessor é '
      '\033[1;33m{}\033[1;34m.'.format(num, antecessor, sucessor))
