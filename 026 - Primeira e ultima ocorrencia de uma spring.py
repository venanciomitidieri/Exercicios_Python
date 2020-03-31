#   Exercício Python 026 - Primeira e última ocorrência de uma string
#   Faça um programa que leia uma frase pelo teclado e mostre:
#       - Quantas vezes aparece a letra 'A'
#       - Em que posição ela aparece a primeira vez
#       - Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).lower().strip()

print("A letra 'a' aparece {} vezes" .format(frase.count('a')))
print('A primeira vez na {} posição' .format(frase.find('a')+1))
print('A ultima vez na {} posição' .format(frase.rfind('a')+1))

