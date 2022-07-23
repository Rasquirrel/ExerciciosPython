# Faça um algoritmo que leia o preço de um produto e depois mostre o novo preço com 5% de desconto
preco = float(input('Por favor, digite o preço do produto desejado e após isso será exibido o preço seguido do '
                    'desconto de 5%')) 

precoDesconto: float = (preco*5)/100
novoPreco = preco - precoDesconto
print('O novo preço é: {}'.format(novoPreco))
