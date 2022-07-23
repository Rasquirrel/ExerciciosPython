# Criar um progama que exija o tanto de reais em uma carteira, e depois mostrar quantos dolares ela pode comprar
# dolar = R$ 3,27
# reais = float(input('Digite a quantidade de reais que você possui: R$'))
# print('Sabendo que um dolar vale R$ 3,27, você pode comprar somente {:.2f}$'.format((reais / 3.27)))

print()
print('Bem vindo usuário! Este progama irá lhe auxiliar em saber se você pode comprar outras moedas com R$.')
dinheiro = float(input('Digite o seu valor: R$ '))

# Conversão

dollar = dinheiro / 5.44
euro = dinheiro / 5.54
yen = dinheiro / 0.04

# Exibição

print('Você pode comprar:\n'
      '{:.2f} Dollars\n'
      '{:.2f} Euros\n'
      '{:.2f} Yenes'.format(dollar, euro, yen))

print('Tenha um bom dia.')
