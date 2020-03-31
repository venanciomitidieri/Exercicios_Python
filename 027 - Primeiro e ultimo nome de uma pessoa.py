#   Exercício Python 027 - Primeiro e último nome de uma pessoa
#   Faça um programa que leia o nome completo de uma pessoa
#   moastrando em seguido o primeiro e ultimo nome separadamente.
nome = input('Digite seu nome completo: ').strip()

dividido = nome.split()

print('Prazer em te conhecer {}' .format(nome))
print('Primeiro nome: {}' .format(dividido[0]))
print('Ultimo nome: {}' .format(dividido[len(dividido) - 1]))


# Sempre é bom dar um .strip para não contar os espaços digitados