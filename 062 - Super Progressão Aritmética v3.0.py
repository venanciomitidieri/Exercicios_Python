#   Exercício Python 062 - Super Progressão Aritmética v3.0
#   Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#   Oprograma encerrará quando ele disser que quer mostrar 0 termos.

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - ' .format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSE')
    mais = int(input('Quantos termos você deseja a mais ? '))
print('Processo finalizado com {} termos de PA' .format(total))
