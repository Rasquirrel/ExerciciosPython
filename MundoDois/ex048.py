'''
Crie um progama que cálcule a soma entre todos os números ímpares
que são multiplos de três e que se encontram entre 1 e 500
'''
# Progama desenvolvido por José Isac
# 29 de julho, 14:28

print('Os números ímpares múltiplos de três entre 1 e 500 são:')
for c in range(1, 501):
    if (c % 3) == 1:
        print(c)
    else:
        continue
    