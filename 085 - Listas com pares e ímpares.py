#   Exercício Python 085 - Listas com pares e ímpares
#   Crie um programa onde o usuário possa digitar sete valores numéricos e
#   cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#   No final, mostre os valores pares e ímpares em ordem crescente

valores = [[], []]
aux = 0
for c in range(0, 7):
    aux = int(input(f'Digite um {c} valor: '))
    if aux % 2 == 0:
        valores[0].append(aux)
    else:
        valores[1].append(aux)

valores[0].sort()
valores[1].sort()
print()
print(f'Os valores pares foram {valores[0]}')
print(f'Os valores imapres foram {valores[1]}')

