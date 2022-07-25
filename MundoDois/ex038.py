# Progama desenvolvido por José Isac
# 25 de julho, 10:31

# Dicionário de cores que eu utilizo para deixar os progamas mais agradáveis
cores = {'Roxa-N': '\033[1;35m',
         'Roxa': '\033[35m',
         'Ciano': '\033[36m',
         'Ciano-N': '\033[1;36m',
         'Azul-N': '\033[1;34m',
         'Azul': '\033[34m',
         'Verde': '\033[32m',
         'Verde-N': '\033[1;32m',
         'Amarelo': '\033[33m',
         'Amarelo-N': '\033[1;33m',
         'Vermelho': '\033[31m',
         'Vermelho-N': '\033[1;31m',
         'Branco-N': '\033[1;30m',
         'Branco': '\033[30m',
         'Close': '\033[m'}

# Cabeçalho
print('-=' * 50)
print('DESAFIO N°38')
print('Escreva um progama que leia dois números inteiros e compare-os\n'
      'mostrando na tela uma mensagem:\n'
      '- O primeiro valor é maior\n'
      '- O segundo valor é maior\n'
      '- Não existe valor maior, os dois são iguais.')
print('-=' * 50)
print()

# Inicio

numeroUm = int(input('Digite um número: '))
numeroDois = int(input('Digite mais um número: '))

# Testes

if numeroUm > numeroDois:
    print('O primeiro valor digitado({})é maior que o segundo({}).'.format(numeroUm, numeroDois))
elif numeroDois > numeroUm:
    print('O segundo valor digitado({}) é maior que o primeiro({}).'.format(numeroDois, numeroUm))
elif numeroUm == numeroDois:
    print('Não existe valor maior, os dois são iguais!')
