# Faça um programa que leia a area de uma parede e exiba a quantidade necessário para pintar a mesma
# sabendo que com 1L de tinta tinta-se 2 metros de parede.

largura = float(input('Digite a largura da parede: '))
comprimento = float(input('Digite o comprimento da parede: '))
area = largura * comprimento
necessario = area / 2

print('A área total é {}' .format(area))
print('Será necessário {} litros de tinta para pintar a parede' .format(necessario))

# CADA LITRO DE TINTA PINTA 2 METROS