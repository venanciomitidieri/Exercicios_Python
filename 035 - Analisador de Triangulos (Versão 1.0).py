#   Exercício Python 035 - Analisando Triângulo v1.0
#   Desenvolva um programa que leia o comprimento de três retas
#   e diga ao usuário se elas podem ou não formar um triângulo.

print('-=-' * 12)
print('Analisador de Triangulos')
print('-=-' * 12)

r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Os seguimentos acima podem formar um triangulo')
else:
    print('Os seguimentos acima não podem formar um triangulo')