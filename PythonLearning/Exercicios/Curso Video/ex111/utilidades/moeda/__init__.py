def aumentar(n, p, c=False):
    res = n + (n * p/100)
    return res if c is False else moeda(res)


def diminuir(n, p, c=False):
    res = n - (n * p/100)
    return res if c is False else moeda(res)


def dobro(n, c=False):
    res = n * 2
    return res if c is False else moeda(res)


def metade(n, c=False):
    res = n / 2
    return res if c is False else moeda(res)


def moeda(n, m='R$'):
    return f'{m}{n:.2f}'.replace('.', ',')


def resumo(n, pa, pd):
    ci = 'R$'
    print('¨' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('¨' * 30)
    print(f"Preço analisado: \t{moeda(n)}")
    print(f"Dobro do preço: \t{dobro(n,True)}")
    print(f"Metade do preço: \t{metade(n, True)}")
    print(f"{pa}% de aumento: \t{aumentar(n,pa,True)}")
    print(f"{pd}% de redução: \t{diminuir(n,pd,True)}")
    print('¨' * 30)
