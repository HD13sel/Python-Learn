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


def leiafloat(msg):
    while True:
        try:
            v = float(input(f'{msg}'))
        except (TypeError, ValueError):
            print('\033[31mErro: Digite um numero real valido.\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mO usuario não digitou!\033[m')
            return 0
        else:
            return v


n = leiaint('Digite um inteiro: ')
f = leiafloat('Digite um real: ')
print(f'Você digitou o inteiro: {n}'
      f'\nVocê digitou o real: {f}')
