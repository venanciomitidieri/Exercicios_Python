#   Exercício Python 066 - Vários números com flag
#   Crie um programa que leia números inteiros pelo teclado.
#   O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#   No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

n = s = cont = 0
while True:   #Quando eu faço esse loop infinito ele fica repetindo até ser falso
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    s += n
#print('A soma vale {}' .format(s))
print(f'A soma vale {s} e você digitou {cont} números')     # Nova forma de escrever uma frase na nova atualização do Python