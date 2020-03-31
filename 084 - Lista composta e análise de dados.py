#   Exercício Python 084 - Lista composta e análise de dados
#   Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#       A) Quantas pessoas foram cadastradas.
#       B) Uma listagem com as pessoas mais pesadas.
#       C) Uma listagem com as pessoas mais leves.

temp = list()
princ = list()
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('peso: ')))
    if len(princ) == 0:
        maio = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    op = str(input('Quer continuar ? '))
    if op in 'Nn':
        break
print('-=' * 30)
print(f'Voce cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
