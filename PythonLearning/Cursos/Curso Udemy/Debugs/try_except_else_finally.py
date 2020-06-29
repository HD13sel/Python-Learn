"""
Try / Except / Else / Finally

Dica de quando e onde tratar códigos:

TODA ENTRADA DEVE SER TRATADA!

OBS: A função do user é DESTRUIR seu sistema!

# Else é executado somente se não ocorrer o erro.
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')

# Finally (SEM GRAÇA)
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')
finally:
    print('Fim')
# OBS: O bloco finally é sempre executado. Independente se houve exceção ou não.
# O finally é geralmente utilizado para fechar ou desalocar recursos.

# Exemplo mais complexo errado


def dividir(a, b):
    return a / b

try:
    num1 = int(input('Informe o primeiro número: '))
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser numérico')
else:
    print(dividir(num1, num2))

# Exemplo mais complexo certo
# OBS: Você é o responsavel pelas entradas das suas funções. Então, trate-as!


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Divisão por zero é nula'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

# Exemplo mais complexo generico

def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um erro'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))


# Exemplo mais complexo semi - generico

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro {err}'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))


"""

