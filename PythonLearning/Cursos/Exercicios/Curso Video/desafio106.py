from time import sleep


def ajuda(texto):
    code = ''

    def padrao(txt, cores):
        nulo = '\033[m'
        if cores == 'verde':
            verd = '\033[30;42m'
            tam = len(txt) + 4
            print('\033[m', end='')
            print(f'{verd}=' * tam)
            print(f"  {txt}  ")
            print(f'=' * tam)
        elif cores == 'azul':
            azu = '\033[30;44m'
            tam = len(txt) + 4
            print(f'{azu}=' * tam)
            print(f"  {txt}  ")
            print(f'=' * tam)
        elif cores == 'verm':
            verm = '\033[30;41m'
            tam = len(txt) + 4
            print(f'{verm}=' * tam)
            print(f"  {txt}  ")
            print(f'=' * tam)
    padrao("SISTEMA DE AJUDA PyHELP", 'verde')
    sleep(1.2)
    code = input(f'\033[m{texto} > ')
    while code != 'fim':
        padrao(f"Acessando o manual do comando '{code}'", 'azul')
        sleep(1.7)
        print('\033[m\033[30m\033[7m')
        help(code)
        sleep(5)
        padrao("SISTEMA DE AJUDA PyHELP", 'verde')
        sleep(1.2)
        code = input(f'\033[m{texto} > ')
        sleep(1.2)
    if code == 'fim':
        padrao('ATÉ LOGO!', 'verm')
        sleep(1)


ajuda('Funcao ou Biblioteca')
