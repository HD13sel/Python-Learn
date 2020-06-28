def leiaint(texto):
    """
    Semelhante a função input() só que apenas aceita apenas um valor numérico.
    :param texto: Texto semelhante a input.
    :return: Retorna mostrando na tela, o valor numerico ou nao.
    """
    v = input(f'{texto}')
    if v.isnumeric():
        v = int(v)
    else:
        while v.isnumeric() is False:
            print('Erro! Digite um numero!')
            v = input('Digite um valor: ')
        v = int(v)
    return v


n = leiaint('Digite um numero: ')
print(f'Você digitou o numero: {n}')
