"""
Faça um progama que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez
e em que posição aparece pela última vez.

Progama desenvolvido por José Isac
21 de julho, 1:52PM
"""
frase = input('Digite uma frase: ').upper()

fraseFix = frase.strip()
quantidadeVezes = fraseFix.count('A')

print('A letra \"A\" aparece {} vezes na frase.'.format(quantidadeVezes))

aparecePrimeiraVez = fraseFix.find('A')

print('A letra \"A\" aparece pela primeira vez na posição: {}'.format(aparecePrimeiraVez + 1))
print('A letra \"A\" aparece pela última vez na posição: {}'.format(fraseFix.rfind('A') + 1))
