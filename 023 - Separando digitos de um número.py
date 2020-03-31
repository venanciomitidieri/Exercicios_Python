num = int(input('Digite um número de 0 a 9999: '))
print('Analisando número {}'.format(num))

n = str(num)

if (num >= 0) and (num <= 9):
    print('Unidade: {}'.format(n[0]))

elif (num >= 10) and (num <= 99):
    print('Unidade: {}'.format(n[1]))
    print('Dezena: {}'.format(n[0]))

elif (num >= 100) and (num <= 999):
    print('Unidade: {}'.format(n[2]))
    print('Dezena: {}'.format(n[1]))
    print('Centena: {}'.format(n[0]))

elif (num >= 1000) and (num <= 9999):
    print('Unidade: {}'.format(n[3]))
    print('Dezena: {}'.format(n[2]))
    print('Centena: {}'.format(n[1]))
    print('Milhar: {}'.format(n[0]))

else:
    print('Número fora do padrão determinado')

# FAZENDO O EXERCICIO SEM OS CONHECIMENTOS DE CONDICIONAIS:

#  num = int(input('Digite um número)
#  u = num // 1 % 10
#  d = num // 10 % 10
#  c = num // 100 % 10
#  m = num // 1000 % 10
#  print('Analisando o numero {}' .format(num))
#  print('A unidade é {}' .format(u))
#  print('A dezena é {}' .format(d))
#  print('A centena é {}' .format(c))
#  print('A milhar é {}' .format(m))

