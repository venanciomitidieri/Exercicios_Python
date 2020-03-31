# Faça um programa que leia um comprimento em metro e exiba seus valores em centimentro e milimetros

valor_metro = float(input('Digite um valor em metro: '))
valor_centimentro = valor_metro * 100
valor_milimetro = valor_metro * 1000

print('O valor de {} em  centimetro é {} e em milimetro é {}' .format(valor_metro, valor_centimentro, valor_milimetro))