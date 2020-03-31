#   Exercício Python 054 - Grupo da Maioridade
#   Crie um programa que leia o ano de nascimento de sete pessoas.
#   No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    idade = atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print('Ao todo tivemos {} maiores de idade' .format(totmaior))
print('Ao todo tivemos {} menores de idade' .format(totmenor))