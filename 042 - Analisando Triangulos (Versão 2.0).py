#   Exercício Python 042 - Analisando Triângulos v2.0
#   Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#       - EQUILÁTERO: todos os lados iguais
#       - ISÓSCELES: dois lados iguais, um diferente
#       - ESCALENO: todos os lados diferentes

print('\033[33m-=-' * 10)
print('Analisando triangulos')
print('\033[33m-=-\033[m' * 10)

r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mOs seguimentos podem formar um triangulo \033[m')
    if r1 == r2 == r3 == r1:
        print('Do tipo Equilatero')
    elif r1 != r2 != r3 != r1:
        print('Do tipo Escaleno')
    else:
        print('Do tipo Isósceles')
else:
    print('\033[31mOs seguimentos não podem formar um triangulo \033[m')
