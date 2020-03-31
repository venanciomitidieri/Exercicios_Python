#   Exercício Python 049 - Tabuada v.2.0
#   Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('\033[31m-=-\033[m' * 10)
print('\033[31mTABUADA !!! \033[m')
print('\033[31m-=-\033[m' * 10)

n = int(input('Digite um número: '))
for c in range(1, 11):
    print("{} x {} = {}".format(n, c, n * c))
    c += 1

print('-' * 10, '\033[33m FIM \033[m', '-' * 10)
