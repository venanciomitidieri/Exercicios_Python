#   Exercício Python 058 - Jogo da Adivinhação v2.0
#   Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
#   Só que agora o jogador vai tentar adivinhar até acertar, #   mostrando no final
#   quantos palpites foram necessários para vencer.

# cores
cor = {'limpa': '\033[m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'lilas': '\033[35m'}

from random import randint
from time import sleep

print('-=-' * 20, )
print('{}JOGO DA ADIVINHAÇÃO {}'.format(cor['vermelho'], cor['limpa']))
print('-=-' * 20)

computador = randint(1, 10)
jogador = -1
tentativa = 0

while jogador != computador:
    jogador = int(input('Em que número eu pensei ? '))
    tentativa += 1

    print('{}Pro{}'.format(cor['verde'], cor['limpa']))
    sleep(1)
    print('{}ce{}'.format(cor['vermelho'], cor['limpa']))
    sleep(1)
    print('{}ssan{}'.format(cor['lilas'], cor['limpa']))
    sleep(1)
    print('{}do{}'.format(cor['azul'], cor['limpa']))

    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez!')
        elif jogador > computador:
            print('Menos... Tente mais uma vez!!')
print('Parabens !! Acertou com {} tentativas'.format(tentativa))

''' from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número de 0 a 10')
print('Será que você consegue adivinhar ?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite ? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez!')
        elif jogador > computador:
            print('Menos... Tente mais uma vez!!')
print('Parabens !! Acertou com {} tentativas' .format(palpites)) '''
