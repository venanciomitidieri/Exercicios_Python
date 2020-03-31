#   Exercício Python 033 - Maior e menor valores
#   Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite um número: '))
num_3 = int(input('Digite um número: '))

if num_1 > num_2 and num_1 > num_3:
    print(num_1, 'É maior que todos')
elif num_2 > num_1 and num_2 > num_3:
    print(num_2, 'É maior que todos')
else:
    print(num_3, 'É maior que todos')