#   Exercício Python 045 - GAME: Pedra Papel e Tesoura
#   Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
jogador = int(input("""[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura
 
 Opção desejada: """))

if jogador > 2 or jogador < 0:
    print('Opção inválida!')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ !!!\n')
    sleep(1)

    print('-=-' * 12)
    print('Jogador jogou: {}' .format(itens[jogador]))
    print('Computador jogou: {}' .format(itens[computador]))
    print('-=-' * 12)

    if jogador == computador:
        print('EMPATE')
    elif jogador == 0 and computador == 1:    # Jogador pedra e computador papel
        print('COMPUTADOR GANHOU')
    elif jogador == 1 and computador == 2:    # Jogador papel e computador tesoura
        print('COMPUTAODR GANHOU')
    elif jogador == 2 and computador == 0:    # Jogador tesoura e computador pedra
        print('COMPUTADOR GANHOU')
    else:
        print('JOGADOR GANHOU')

