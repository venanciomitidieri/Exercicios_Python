#   Crie um programa que leia dois valores e mostre um menu na tela:
#       [ 1 ] somar
#       [ 2 ] multiplicar
#       [ 3 ] maior
#       [ 4 ] novos números
#       [ 5 ] sair do programa
#   Seu programa deverá realizar a operação solicitada em cada caso.

valor_1 = int(input('Digite um valor: '))
valor_2 = int(input('Digite um valor: '))
op = 0

while op != 5:
    print('=-' * 15)
    print('''    [1] - somar
    [2] - multiplicar
    [3] - maior
    [4] - novos números
    [5] sair do programa''')
    print('=-' * 15)

    op = int(input('>>>>>> Opção desejada: '))

    if op == 1:
        print('Resultado: {} + {} = {}' .format(valor_1, valor_2, valor_1 + valor_2))
    elif op == 2:
        print('Resultado: {} * {} = {}' .format(valor_1, valor_2, valor_1 * valor_2))
    elif op == 3:
        print('Resultado: Entre {} e {} o maior valor é {}' .format(valor_1, valor_2, valor_1 if valor_1 > valor_2 else valor_2))
    elif op == 4:
        valor_1 = int(input('Digite um valor: '))
        valor_2 = int(input('Digite um valor: '))
    elif op < 1 or op > 5:
        print('Valor incorreto, por favor digitar um valor correto')
