# Faça um programa que leia um número e exiba quanto pode ser comprado de dolar e euro

dinheiro = float(input('Quanto você tem na carteira? R$ '))
dolar = dinheiro / 3.27
euro = dinheiro / 4.59
print('Com a quantia que você possui você pode comprar {:.2f} dólares. \nE pode comprar {:.2f} de euro' .format(dolar, euro))