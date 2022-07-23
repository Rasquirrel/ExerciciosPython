# Progama desenvolvido por José Isac
# 20 de julho, 4:40 PM

# Este progama irá perguntar a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele
# foi alugado. Após isso irá calcular o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print()
print('Bem vindo usuário!')

# Variáveis

kmPercorridos = float(input('Informe a quantidade de Km percorridos: '))
diasAlugado = int(input('Informe a quantidade de dias no qual o carro foi alugado: '))
precoAPagar = (60 * diasAlugado) + (0.15 * kmPercorridos)

# Resultado

print('Será necessário pagar R${:.2f}'.format(precoAPagar))
