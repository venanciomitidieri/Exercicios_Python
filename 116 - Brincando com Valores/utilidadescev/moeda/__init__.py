def metade(num=0, formato=False):
    res = num / 2
    return res if not formato else moeda(res)


def dobro(num=0, formato=False):
    res = num * 2
    return num if not formato else moeda(res)


def aumentar(num=0, taxa=0, formato=False):
    res = num + (num * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(num=0, taxa=0, formato=False):
    res = num - (num * taxa/100)
    return res if formato is False else moeda(res)


def moeda(num=0, moeda='R$'):
    return f'{moeda} {num:>2f}' .replace('.', ',')


def resumo(num=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR' .center(30))
    print('-' * 30)
    print(f'Preço analizado: \t\t{moeda(num)}')
    print(f'Dobro do preço: \t\t{dobro(num, True)}')
    print(f'Metade do preço: \t\t{metade(num, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(num, taxaa, True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(num, taxar, True)}')
    print('-' * 30)
