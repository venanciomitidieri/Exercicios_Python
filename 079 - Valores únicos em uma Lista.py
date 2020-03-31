#   Exercício Python 079 - Valores únicos em uma Lista
#   Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#   Caso o número já exista lá dentro, ele não será adicionado.
#   No final, serão exibidos todos os valores únicos digitados, em ordem crescente

numeros = list()
while True:
    aux = int(input('Digite um valor: '))
    if aux not in numeros:
        numeros.append(aux)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar')
    op = str(input('Quer continuar? ')).strip().upper()
    if op in 'N':
        break
print('-=' * 30)
numeros.sort()
print(f'Valores digitados: {numeros}')
