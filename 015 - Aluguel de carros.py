# Faça um programa que leia a quantidade de km rodados por um carro e quantos dias foi alugado e exiba o valor total
# sabendo que a diaria custa 60 reais e a quilometragem 0.15

km = float(input('Qual a quilometragem rodada? '))
dias = int(input('Quantos dias de aluguel? '))

km_valor = km * 0.15
aluguel_dia = dias * 60
total = km_valor + aluguel_dia

print('O valor total do aluguel sera {} reais' .format(total))
