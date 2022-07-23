# Escreva um progama que leia um valor em metros e o exiba convertido em centímetros e milímetros e nas outras medidas
comprimento = float(input('Digite o comprimento em metros: '))
dm = comprimento * 10
cm = comprimento * 100
mm = comprimento * 1000
km = comprimento / 1000
hm = comprimento / 100
dam = comprimento / 10

print('A medida {}m equivale a:'.format(comprimento))
print('{}Km;'.format(km))
print('{}Hm;'.format(hm))
print('{}Dam;'.format(dam))
print('{:.0f}Dm;'.format(dm))
print('{:.0f}cm;'.format(cm))
print('{:.0f}mm;'.format(mm))

#:.0f faz com que eu remova as casas decimais
