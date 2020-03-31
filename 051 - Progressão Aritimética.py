#   Exercício Python 051 - Progressão Aritmética
#   Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#   No final, mostre os 10 primeiros termos dessa progressão.

print("=" * 20)
print("PROGRESSÃO DE UMA PA")
print("=" * 20)

termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = termo + 10 * razao                    # formula matemética para se achar o décimo termo

for i in range(termo, decimo, razao):          # Números que serão colocados no input
    print(i, end=' -> ')
print("FIM")
