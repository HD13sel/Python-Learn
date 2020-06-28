"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo
assim que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.

A fomra geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema


# Exemplo 1 - Tratando um erro genérico

try:
    geek()
except:
    print('Deu algum problema')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

OBS: Tratar erros de forma genérica não é melhor forma de tratamento de erros. O ideal é SEMPRE tratar de
forma específica.

# Exemplo 2 - Tratando um erro específico

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente.')

# Exemplo 3 - Tratando um erro específico

try:
    len(5)
except TypeError:
    print('Você está utilizando uma função inexistente.')

# Exemplo 4 - Tratando um erro específico com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')


# Exemplo 5
# Podemos efetuar diversos tratamentos de erros de uma vez.

try:
    # len(5)
    # geek()
    print('Geek'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except IndexError as errc:
    print(f'Deu IndexError: {errc}')
except:
    print('Deu um erro diferente')

"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None
    except NameError:
        return None


dic = {"nome": "Henrique"}
print(pega_valor(2, "nme"))

