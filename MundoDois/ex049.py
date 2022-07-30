numero = int(input('Digite o número no qual você precisa ver a tabuad: '))

calc = 0
i = 0
for c in range(1, 11):
    i += 1
    calc = numero  * i
    print(f'{numero} x {i} = {calc}')
