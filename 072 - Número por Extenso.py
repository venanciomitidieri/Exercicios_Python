#   Exercício Python 072 - Número por Extenso
#   Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#   Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numero = ('zero', 'um', 'dois', 'três', 'quatro',
          'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze',
          'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
          'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o numero {numero[num]}')
    else:
        print('Tente novamente.Digite um número entre 0 e 20: ')
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
print('FIM')