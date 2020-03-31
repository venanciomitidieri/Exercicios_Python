#   Exercício Python 053 - Detector de Palíndromo
#   Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):   # Ele usa o len -1  para pegar a ultima letra da string, usa o -1 novamente pra pegar até o primeiro numero que seria zero
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('É um palindromo!')
else:
    print('Não é um palindromo!')