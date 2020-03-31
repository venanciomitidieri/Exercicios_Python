#   Exercício Python 089 - Boletim com listas compostas
#   Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#   No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
#   as notas de cada aluno individualmente.

boletin = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('1ª Nota: '))
    n2 = float(input('2ª Nota: '))
    media = (n1 + n2) / 2
    boletin.append([nome, [n1, n2], media])
    op = str(input('Continuar? [S/N] ')).strip().upper()
    if op == 'N':
        break
print('-=' * 25)
print(f'{"Nª":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 25)
for i, v in enumerate(boletin):
    print(f'{i:<4}{v[0]:<10}{v[2]:>8.1f}')
while True:
    print('-' * 30)
    ref = int(input('Mostrar notas de qual aluno ? (999 interrompe)'))
    if ref == 999:
        break
    print(f'Notas do(a) {boletin[ref][0]} são: {boletin[ref][1]}')
print('<<< VOLTE SEMPRE >>>')