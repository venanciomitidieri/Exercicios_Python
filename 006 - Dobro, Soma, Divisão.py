# Faça um programa que leia um número e depois exiba sua soma, subtração, divisão, divisão inteira e exponencial

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
soma = n1 + n2
sub = n1 - n2
d = n1 / n2
m = n1 * n2
di = n1 // n2
e = n1 ** n2
# print('A soma entre', numero1, 'e', numero2, 'vale: {}'.format(soma))
# print('A soma entre {} e {} vale {}' .format(n1, n2, soma))
# print('A subtração entre {} e {} vale {}' .format(n1, n2, sub))
# print('A multiplicação entre {} e {} vale {}' .format(n1, n2, m))
# print('A divisão entre {} e {} vale {}' .format(n1, n2, d))
# print('A divisão inteira entre {} e {} vale {}' .format(n1, n2, di))
# print('A exponencial entre {} e {} vale {}' .format(n1, n2, e))

# Para não fazer esse monte de print eu posso usar o \n para pular linha no mesmo print, Vamos lá.

print('A soma é {}, \n A subtração é {}, \n A multiplicação é {}, \n A divisão é {}, \n A divisão inteira é {}, '
      '\n A exponencial é {}' .format(soma, sub, m, d, di, e))

# No lugar de virgulas e aspas simples coloco o colchetes e depois coloco na ordem as informações que serão preenchidas