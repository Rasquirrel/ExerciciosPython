# Progama desenvolvido por José Isac
# 22 de julho, 12:04
# Este progama tem como objetivo exibir a tabuada de multiplicar de qualquer número que o usuário deseje

print()
print('\033[1;33m-=' * 50)
print('DESAFIO N° 9')
print('\033[1;35mDesenvolver um aplicativo que mostre a tabuada de multiplicar de um número de preferência do usuário.')
print('\033[1;33m-='*50)
print()

num = int(input('\033[1;34mDigite um número para ver sua tabuada: '))
print('\033[1;32m_' * 25)

print('\t\033[1;30m{} \033[1;34mx  \033[1;33m1  \033[1;34m= \033[1;31m{}\n'
      '\t\033[1;30m{} \033[1;34mx  \033[1;33m2  \033[1;34m= \033[1;31m{}\n'
      '\t\033[1;30m{} \033[1;34mx  \033[1;33m3  \033[1;34m= \033[1;31m{}\n'
      '\t\033[1;30m{} \033[1;34mx  \033[1;33m4  \033[1;34m= \033[1;31m{}\n'
      '\t\033[1;30m{} \033[1;34mx  \033[1;33m5  \033[1;34m= \033[1;31m{}\n'
      '\t\033[1;30m{} \033[1;34mx  \033[1;33m6  \033[1;34m= \033[1;31m{}\n'
      '\t\033[1;30m{} \033[1;34mx  \033[1;33m7  \033[1;34m= \033[1;31m{}\n'
      '\t\033[1;30m{} \033[1;34mx  \033[1;33m8  \033[1;34m= \033[1;31m{}\n'
      '\t\033[1;30m{} \033[1;34mx  \033[1;33m9  \033[1;34m= \033[1;31m{}\n'
      '\t\033[1;30m{} \033[1;34mx  \033[1;33m10 \033[1;34m= \033[1;31m{}'.format(num, (num * 1), num, (num * 2), num, (num * 3), num, (num * 4), num, (num * 5), num, (num * 6), num, (num * 7), num, (num * 8), num, (num * 9), num, (num * 10)))

print('\033[1;32m_' * 25)
