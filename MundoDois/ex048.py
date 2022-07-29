'''
Crie um progama que cálcule a soma entre todos os números ímpares
que são multiplos de três e que se encontram entre 1 e 500
'''
# Progama desenvolvido por José Isac
# 29 de julho, 14:28

print('Os números ímpares múltiplos de três entre 1 e 500 são:')
for c in range(3, 499, 3):
    if c % 2 == 1:
        print(c)
        