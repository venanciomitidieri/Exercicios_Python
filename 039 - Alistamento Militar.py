#   Exercício Python 039 - Alistamento Militar
#   Faça um programa que leia o ano de nascimento de um jovem
#   e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#   se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#   Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_nascimento = int(input(' Digite o ano em que nasceu: '))
idade = date.today().year - ano_nascimento

print('\033[33m Você tem {} anos \033[m' .format(idade))

if idade < 18:
    print('Ainda não está no tempo de se alistar. Faltam {} anos para o alistamento obrigatório' .format(18 - idade))
elif idade == 18:
    print('Esta na hora de se alistar !!')
else:
    print('\033[31m Já passou {} anos do seu alistamento obrigatório !!! \033[m' .format(idade - 18))
