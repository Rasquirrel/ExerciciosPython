# Programa desenvolvido por José Isac
# 13:55 20 de agosto

print('Este programa irá lhe ajudar a exibir os dez primeiros termos de uma progressão aritmética.')
prim_Termo = int(input('Digite o valor do primeiro termo da P.A: '))
razao = int(input('Digite o valor da razão da P.A: '))
decimo_Termo = prim_Termo + 9 * razao

for termos in range(prim_Termo, decimo_Termo + razao , razao):
    print(termos)
