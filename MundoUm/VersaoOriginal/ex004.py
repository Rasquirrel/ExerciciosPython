# Progama desenvolvido por José Isac
# 19 de julho, 7:44 PM
#
# Este progama vai dizer todas as informações sobre o valor associado a uma variável

algo = input('Digite algo: ')

print('O tipo primivito é: ')
print(type(algo))

print('É alfabetico?')
print(algo.isalpha())

print('É númerico?')
print(algo.isnumeric())

print('É alfanúmerico?')
print(algo.isalnum())

print('Está presente na tabela ascii?')
print(algo.isascii())

print('É digito?')
print(algo.isdigit())

print('É decimal?')
print(algo.isdecimal())

print('É um identificador?')
print(algo.isidentifier())

print('Está escrito em letras minúsculas?')
print(algo.islower())

print('Está escrito em letras maiúsculas?')
print(algo.isupper())

print('É imprimivel?')
print(algo.isprintable())

print('É somente espaço?')
print(algo.isspace())

print('É um título?')
print(algo.istitle())
