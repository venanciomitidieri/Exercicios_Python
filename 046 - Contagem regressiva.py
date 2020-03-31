#   Exercício Python 046 - Contagem regressiva
#   Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
#   indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
print('\033[31mCONTAGEM REGRESSIVA PARA O ANO NOVO \033[m')

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[33mFELIZ ANO NOVO !!! \033[m')
