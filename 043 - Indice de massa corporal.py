#   Exercício Python 043 - Índice de Massa Corporal
#   Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
#   e mostre seu status, de acordo com a tabela abaixo:
#       - IMC abaixo de 18,5: Abaixo do Peso
#       - Entre 18,5 e 25: Peso Ideal
#       - 25 até 30: Sobrepeso
#       - 30 até 40: Obesidade
#       - Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura**2)

if imc < 18.5:
    print('\033[31mATENÇÃO !! ABAIXO DO PESO \033[m')
elif imc >= 18.5 and imc < 25:
    print('\033[32mPARABÉNS! Peso ideal \033[m')
elif imc >= 25 and imc <= 30:
    print('\033[33m Sobrepeso \033[m')
elif imc > 30 and imc <= 40:
    print('\033[33m Obesidade \033[m')
else:
    print('\033[31m MUITA ATENÇÃO !!! OBESIDADE MORBIDA')


