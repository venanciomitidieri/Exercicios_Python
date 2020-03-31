#   Exercício Python 096 - Função que calcula área
#    Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
#    (largura e comprimento) e mostre a área do terreno.

def area():
    print('Controle de Terrenos')
    print('---------------------')
    l = float(input('LARGURA (m): '))
    c = float(input('COMPRIMENTO (m): '))
    d = l * c
    print(f'A área de um terreno {l} x {c} é de {d} metros quadrados')


area()
