#   Exercício Python 081 - Extraindo dados de uma Lista
#   Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#       A) Quantos números foram digitados.
#       B) A lista de valores, ordenada de forma decrescente.
#       C) Se o valor 5 foi digitado e está ou não na lista.

valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
print('-=' * 30)
print(f'Os valores digitados foram: {valores}')
print(f'O tamanho da lista é: {len(valores)}')
valores.sort(reverse=True)
print(f'A lista em ordem descresente será: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
