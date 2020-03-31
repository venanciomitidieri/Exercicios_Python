#   Crie um programa que vai ler vários números e colocar em uma lista.
#   Depois disso, crie duas listas extras que vão conter apenas os valores pares e
#   os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    op = str(input('Deseja continuar ? [S/N] ')).strip().upper()
    if op in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'a lista complesta é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')