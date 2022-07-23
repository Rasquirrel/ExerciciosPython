"""
Crie um progama que leia o nome completo de uma pessoa, e apareça na tela, o nome com todas as letras minusculas
o nome com todas as letras maiusculas, quantas letras ao todo sem considerar
os espaços e quantas letras tem o primeiro nome.
"""
"""
Progama desenvolvido por José Isac
21 de julho, 1:31 PM
"""

nome = input('Por favor, digite o seu nome completo: ').strip()
print('Seu nome com todas as letras maiúsculas é: ', nome.upper())
print('Seu nome com todas as letras minúsculas é: ', nome.lower())

nomeSemEspaco = (len(nome)) - (len(nome.split()) - 1)
nomeDividido = nome.split()
primeiroNome = nomeDividido[0]
letrasPrimeiroNome = len(primeiroNome)

print('A quantidade de letras que seu nome possuí é: ', nomeSemEspaco)
print('A quantidade de letras do primeiro nome é: ', letrasPrimeiroNome)
