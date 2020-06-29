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
