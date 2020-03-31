# Faça um programa que leia um valor e exiba seu valor com desconto de 5%

valor = float(input('Digite o valor do produto sem desconto: R$ '))
valor_desconto = valor * 0.05
valor_final = valor - valor_desconto

print('O valor do produto com desconto é {}' .format(valor_final))