#   Exercício Python 060 - Cálculo do Fatorial
#   Faça um programa que leia um número qualquer e mostre o seu fatorial.
#   Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}' .format(n, f))


'''  print("--- CÁLCULO DO FATORIAL ---")
num = int(input("Digite o número: "))
fat = 1
print("Calculando {}! =".format(num), end=' ')
while num > 0:
    if num == 1:
        print(num, end=' ')
    else:
        print(num, end=' x ')
    fat *= num
    num -= 1
print("= {}".format(fat))  '''