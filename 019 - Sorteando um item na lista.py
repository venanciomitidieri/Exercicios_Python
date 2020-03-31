import random
primeiro_nome = input('Digite o primeiro nome: ')
segundo_nome = input('Digite o segundo nome: ')
terceiro_nome = input('Digite o terceiro nome: ')
quarto_nome = input('Digite o quarto nome: ')

lista = [primeiro_nome, segundo_nome, terceiro_nome, quarto_nome]
print('Dos nomes {}, {}, {}, {}. O aluno escolhido foi {}' .format(primeiro_nome, segundo_nome, terceiro_nome, quarto_nome,
random.choice(lista)))


