#   Exercício Python 056 - Analisador completo
#   Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#   No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
#   e quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher_20 = 0

for p in range(1, 5):
    print('=' * 5, '{} pessoa' .format(p), '=' * 5)
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:  # Colocamos 'Mn' para o leitor reconhecer tanto o minusculo quanto maiusculo
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:     # Colocamos 'Ff' para o leitor reconhecer tanto o minusculo quanto maiusculo
        totmulher_20 += 1
mediaidade = somaidade / 4
print('A media das idades é {} anos' .format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}' .format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos' .format(totmulher_20))
