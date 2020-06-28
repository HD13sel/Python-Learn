"""
Módulos Collections - Named Tuple

# Recap tuple
tupla = (1, 2, 3)

print(tupla[1])

Named Tuple -> São tuple diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.

"""

# Importando

from collections import namedtuple

# Precisamos definir o nome e parâmetros

# Forma 1

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando
ray = cachorro(idade=2, raca='ChowChow', nome='Ray')

print(ray)

# Acessando os dados

# Forma 1
print(ray[0])  # idade
print(ray[1])  # raca
print(ray[2])  # nome

# Forma 2
print(ray.idade)  # idade
print(ray.raca) # raca
print(ray.nome)  # nome

print(ray.index('ChowChow'))

print(ray.count('ChowChow'))
