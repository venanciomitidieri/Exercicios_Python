#   Exercício Python 091 - Jogo de Dados em Python
#   Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#   Guarde esses resultados em um dicionário em Python.
#   No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogadas = dict()
jogadas['jogador_1'] = randint(1, 6)
jogadas['jogador_2'] = randint(1, 6)
jogadas['jogador_3'] = randint(1, 6)
jogadas['jogador_4'] = randint(1, 6)

ranking = list()
print('Valores Sorteados')
for k, v in jogadas.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print(ranking)
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f' {i+1}ª lugar: {v[0]} com {v[1]}.')
    sleep(1)