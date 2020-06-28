"""
Debuggando com PDB

PDB -> Python Debugger
Bug = Inseto

# OBS: A utilização do print() para debuggar o código é uma prática ruim

def dividir(a, b):
    print(f'a = {a}, b = {b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro {err}'

print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger
# Em Python, podemos fazer isso em diferentes IDEs, como o PyCharm ou utilizando
# o PDB - Python Debugger
# Exemplo com PyCharm


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro {err}'

print(dividir(4, 0))

# Exemplo com o PDB - Python Debugger - Exemplo 1
# Para utilizar o PDB, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()
# Comandos básicos do PDB:
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime a variável)
# c (continua a execução - finaliza o debugging)

import pdb

nome = 'Henrique'
sobrenome = 'Diesel'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Exemplo com o PDB - Python Debugger - Exemplo 2


nome = 'Henrique'
sobrenome = 'Diesel'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por que utilizar esse formato?
# O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas
# no inicio do arquivo. Por isso, ao invés de colocarmos o import do pdb no início do arquivo.
# Colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção.


# Exemplo com o PDB - Python Debugger - Exemplo 3
# Exemplo 1 :(precisamos*)
# A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi incorporado como
# função built-in(integrado) chamada breakpoint()
nome = 'Henrique'
sobrenome = 'Diesel'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)

# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos pdb
def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(soma(1, 3, 5, 7))

# Como os nomes das var são os mesmo dos comandos do pdb, devemos utilizar o comando p para imprimir as var.
# Nada de colocar nomes não representativos em var. Sempre optar por nomes significativos.

def soma(num1, num2, num3, num4)
    breakpoint()
    return num1, num2, num3, num4
"""



