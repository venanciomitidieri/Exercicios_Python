#   Exercício Python 097 - Um print especial
#    Faça um programa que tenha uma função chamada escreva(),
#    que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(a):
    tam = len(a) + 4
    print('~' * tam)
    print(f'  {a}')
    print('~' * tam)


escreva('Curso em Python no Youtube')
escreva('CiV')
escreva('Venancio Mota Mitidieri')
