# Fazer um progama que mostre na tela uma contagem regressiva de 10 segundos para o estouro
# de fogos de artifício

# Progama desenvolvido por José Isac
# 29 de julho, 13:30

from time import sleep
import emoji

a = True

while a == True:
    print('Os fogos de artifícios irão estourar!')
    for c in range(1, 11, -1):
        print(c)
        sleep(1)
    print('POOW! :fireworks:')
    sleep(3)
    print('POOOW!!! :fireworks:')
    sleep(3)
    print('CABUMM! :fireworks:')
    sleep(2)
    print('POOoW!!!!:fireworks: POW!! :fireworks:')
    sleep(6)
    print('POOOOOOOOOWW! :fireworks: :fireworks: :fireworks: :fireworks:')
    sleep(1)

    d = input('Deseja voltar no tempo e ver novamente? -- Sim / Nao').lower().strip()
    
    if d == 'sim':
        print('🕐')
        sleep(1)
        print('🕑')
        sleep(1)
        print('🕐')
        continue
    else:
        exit()

