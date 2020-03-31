#   Exercício Python 087 - Mais sobre Matriz em Python
#    Aprimore o desafio anterior, mostrando no final:
#       A) A soma de todos os valores pares digitados.
#       B) A soma dos valores da terceira coluna.
#       C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = maior = scol = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para[{i}, {j}] = '))
print('-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            spar += matriz[i][j]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for i in range(0, 3):
    scol += matriz[i][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for j in range(0, 3):
    if j == 0:
        maior = matriz[1][j]
    elif matriz[1][j] > maior:
        maior = matriz[1][j]
print(f'A maior valor da segunda linha é {maior}')
