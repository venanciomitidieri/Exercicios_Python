#   Exercício Python 034 - Aumentos múltiplos
#   Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#   Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu sálario: R$ '))

if salario >= 1250:
    novo_salario = salario * 1.1
    print('Seu aumento foi de {:.2f}, ficando um total de {:.2f}' .format(salario * 0.1, novo_salario))
else:
    novo_salario = salario * 1.15
    print('Seu aumento foi de {:.2f}, ficando um total de {:.2f}' .format(salario * 0.15, novo_salario))
