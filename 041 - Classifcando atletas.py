#   Exercício Python 041 - Classificando Atletas
#   A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
#   e mostre sua categoria, de acordo com a idade:
#       - Até 9 anos: MIRIM
#       - Até 14 anos: INFANTIL
#       - Até 19 anos: JÚNIOR
#       - Até 25 anos: SÊNIOR
#       - Acima de 25 anos: MASTER

from datetime import date

ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
print('O atleta tem: {} anos' .format(idade))
if idade <= 9:
    print('\033[33m Sua categoria é MIRIM \033[m')
elif idade > 9 and idade <= 14:
    print('\033[33m Sua categoria é INFANTIL \033[m')
elif idade > 14 and idade <= 19:
    print('\033[33m Sua categoria é JUNIOR \033[m')
elif idade > 19 and idade <= 20:
    print('\033[33m Sua categoria é SENIOR \033[m')
else:
    print('\033[33mSua categoria é MASTER \033[m')