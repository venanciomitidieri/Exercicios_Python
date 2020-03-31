#   Exercício Python 022 - Analisador de Textos
#   Crie um programa que leia o nome completo de uma pessoa e mostre:
#       - O nome com todas as letras maiúsculas e minúsculas.
#       - Quantas letras ao todo (sem considerar espaços).
#       - Quantas letras tem o primeiro nome.


nome = str(input('Digite seu nome: ')).strip()
print('O nome com letras maiúsculas: {}'.format(nome.upper()))
print('O nome com letras minúsculas: {}'.format(nome.lower()))
print('O nome tem {} letras' .format(len(nome) - nome.count(' ')))
dividido = nome.split()
print('O seu primeiro nome tem: {}'.format(len(dividido[0])), 'letras')

