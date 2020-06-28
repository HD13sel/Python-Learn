def fatorial(num, show=False):
    """
    Calcula o fatorial de um numero.
    :param num: O numero a ser Calculado
    :param show: (opcional) Mostrar ou não o rascunho.
    :return: O valor do fatorial do valor num.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show is True:
            if c > 1:
                print(f'{c} X', end=' ')
            if c == 1:
                print(f'{c}', end=' ')
                print('=', end=' ')
    return f


help(fatorial)
