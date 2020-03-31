#   Exercício Python 044 - Gerenciador de Pagamentos
#   Elabore um programa que calcule o valor a ser pago por um produto,
#   considerando o seu preço normal e condição de pagamento:
#       - à vista dinheiro/cheque: 10% de desconto
#       - à vista no cartão: 5% de desconto
#       - em até 2x no cartão: preço formal
#       - 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS VENANCIO '))

preco = float(input('Digite o valor do produto: R$ '))
pagamento = int(input("""1 - Dinheiro/Cheque.
2 - Cartão a vista.
3 - Cartão 2x.
4 - Cartão 3x ou mais 
Escolha uma forma de pagamento: """))

if pagamento == 1:
    total = preco - (preco * 0.1)
    print('O valor total será de {} reais' .format(total))
elif pagamento == 2:
    total = preco - (preco * 0.05)
    print('O valor total será de {} reais' .format(total))
elif pagamento == 3:
    total = preco
    print('O valor total será de {} reais' .format(total))
elif pagamento == 4:
    total = preco * 1.2
    totpar = int(input('Quantas parcelas? '))
    parcela = total / totpar
    print('O valor total será de {:.2f} dividido em {} com parcelas de {:.2f}' .format(total, totpar, parcela))
else:
    print('Forma de pagamento inválida')
