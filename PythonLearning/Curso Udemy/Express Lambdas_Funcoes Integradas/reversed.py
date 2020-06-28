"""
Reversed

OBS: Não confunda com a função reverse() que estudamos na listas. Só funciona em listas.

Já a função reversed() funciona com qualquer iterável.

Sua função é inverter o iterável.

A função reversed() retorna um iterável chamdo List Reverse Iterator
"""

# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para uma list, tuple ou set.

# list
print(list(reversed(lista)))

# tuple
print(tuple(reversed(lista)))

# set
print(set(reversed(lista)))  # Set não define a ordem dos elementos.

# Podemos iterar sobre o reversed()
for letra in reversed('Henrique Diesel'):
    print(letra, end='')

print('\n')
# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Henrique Diesel'))))

# Já vimos como fazer isso mais facil com slice de strings
print('Henrique Diesel'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

print('\n')
# Apesar que também já vimos como fazer isso utilizando o próprio range()
for n in range(9, -1, -1):
    print(n)




