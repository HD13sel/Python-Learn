def leiadinheiro(val):
    valido = False
    while not valido:
        valor = str(input(f'{val}').replace(',', '.')).strip()
        if valor.isalpha() or valor == '':
            print(f'\033[31mErro. "{valor}" é invalido. Digite um valor numérico.\033[m')

        else:
            valido = True
            return float(valor)


