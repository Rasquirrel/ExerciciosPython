# Progama desenvolvido por José Isac
# 23 de julho,  16:56
# Progama com o objetivo de exibir informações e realizar algumas transformações com um nome

print()
print('\033[1;33m-=' * 50)
print('Desafio N° 22')
print('\033[1;35mDesenvolva um aplicativo que receba o nome completo de uma pessoa.\n'
      'Exiba o nome com todas as letras minúsculas, maiúsculas, a quantidade de letras\n'
      'que o nome possui sem contar os espaços e quantas letras tem o primeiro nome.')
print('\033[1;33m-=' * 50, '\033[m')
print()

nome = str(input('\033[1;34mDigite o seu nome: '))
nomeLetrasMa = nome.upper()
nomeLetrasMi = nome.lower()
nomeQuantLetras = (len(nome)) - (len(nome.split()) - 1)
nomeDividido = nome.split()
primeiroNomeQuantLetras = len(nomeDividido[0])

print('\033[1;34mNome com letras minúsculas: \033[1;31m{}'.format(nomeLetrasMi))
print('\033[1;34mNome com letras maiúsculas: \033[1;31m{}'.format(nomeLetrasMa))
print('\033[1;34mQuantidade de letras do nome todo: \033[1;31m{}'.format(nomeQuantLetras))
print('\033[1;34mQuantidade de letras do primeiro nome: \033[1;31m{}'.format(primeiroNomeQuantLetras))
