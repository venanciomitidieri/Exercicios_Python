#   Exercício Python 005 - Antecessor e Sucessor
#   Faça um programa que leia um número Inteiro
#   e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
# a = n -1
# s = n + 1
# print('O antecessor é {} e o sucessor é {}' .format(a, s))

# No exemplo acima foi usado três variaveis, isso é bom para quando eu for utiliza-lás novamento,
# como isso não será necessário nesse programa, vamos fazer com uma so variavel

print('O antecessor é {} e o sucessor é {}' .format(n-1, n+1))