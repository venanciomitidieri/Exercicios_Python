#   Exercício Python 070 - Estatísticas em produtos
# #   Crie um programa que leia o nome e o preço de vários produtos.
# #   O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# #       A) qual é o total gasto na compra.
# #       B) quantos produtos custam mais de R$1000.
# #       C) qual é o nome do produto mais barato.

print('-' * 30)
print('LOJA DO BARATÃO')
print('-' * 30)

total = tot1000 = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    cont += 1
    total += preco
    if preco > 1000:
        tot1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}' .format('FIM DO PROGRAMA'))
print(f'O total de compras foi: {total:.2f}')
print(f'O número de produtos acima de R$ 1.000: {tot1000}')
print(f'O produto mais barato foi {barato} que custa R$ {menor}')
