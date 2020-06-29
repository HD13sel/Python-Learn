def linha(tam = 50):
    return '-' * tam


def titulo(txt):
    print(linha())
    print(txt.center(50))
    print(linha())


def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua opção:\033[m ')
    return opc


def leiaint(msg):
    while True:
        try:
            v = int(input(f'{msg}'))
        except (TypeError, ValueError):
            print('\033[31mErro: Digite um numero inteiro valido.\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mO usuario não digitou!\033[m')
            return 0
        else:
            return v
