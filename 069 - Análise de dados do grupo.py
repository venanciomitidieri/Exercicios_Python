#   Crie um programa que leia a idade e o sexo de várias pessoas.
#   A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#       A) quantas pessoas tem mais de 18 anos.
#       B) quantos homens foram cadastrados.
#       C) quantas mulheres tem menos de 20 anos.

print('-' * 20)
print('CADASTRANDO PESSOAS')
print('-' * 20)

tot18 = 0
tothomens = 0
totmulher_and_maior20anos = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        tot18 += 1
    if sexo == 'M':
        tothomens += 1
    if sexo == 'f' and idade > 20:
        totmulher_and_maior20anos += 1
    print('-' * 20)
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Você deseja continuar ? [S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
print('Acabou!')
print(f'Pessoas com mais de 18 anos: {tot18}')
print(f'Pessoas do sexo masculino: {tothomens}')
print(f'Pessoas do sexo feminino com mais de 20 anos: {totmulher_and_maior20anos}' )