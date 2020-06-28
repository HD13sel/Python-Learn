"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá de qualquer coisa, desde com asterisco (*)

Exemplo:
*xis

Mas por convenção, utilizamos *args para defini-lo

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla.
Então desde já lembre-se que tuplas são imutáveis.

# Exemplos

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9))

# Entendendo o *args


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(3, 4, 5, 6))

print(soma_todos_numeros('a'))  # TypeError
print(soma_todos_numeros(23.4, 12.5))


def soma_todos_numeros(nome, email, *args):
    return sum(args)


print(soma_todos_numeros('Henrique', 'Gmail'))
print(soma_todos_numeros('Henrique', 'Gmail', 1))
print(soma_todos_numeros('Henrique', 'Gmail', 2, 3))
print(soma_todos_numeros('Henrique', 'Gmail', 2, 3, 4))
print(soma_todos_numeros('Henrique', 'Gmail', 3, 4, 5, 6))

print(soma_todos_numeros('a'))  # TypeError
print(soma_todos_numeros('Henrique', 'Gmail', 23.4, 12.5))

# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Henrique' in args and 'Diesel' in args:
        return 'Bem-vindo Henrique'
    return 'Eu não tenho certeza quem você é...'

print(verifica_info())
print(verifica_info(1, True, 'Diesel', 'Henrique'))
print(verifica_info(1, "Diesel", 3.145))
"""

def soma_todos_numeros(*args):
    return sum(args)


# print(soma_todos_numeros())
# print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempactador
print(soma_todos_numeros(*numeros))

# OBS: O asterisco serve para que informamos ao Python que estamos passando como argumento uma coleção de dados.
# Desta forma, ele saberá que precisará antes de desempacotar estes dados.


