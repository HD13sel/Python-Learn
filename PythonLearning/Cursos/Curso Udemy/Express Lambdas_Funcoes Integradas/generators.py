"""
Generators Expression

Em aulas anteriores nós estudamos:
- List Comprehension;
- Dict Comprehension;
- Set Comprehension;

Não vimos:
- Tuple comprehension ... porque elas se chamam Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any[nome[0] == 'C' for nome in nomes])

# Poderiamos ter feito utilizando Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

import sys

# Qual é a utilidade de getsizeof()? -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro
from sys import getsizeof

# Mostra quantos bytes a string está ocupando em memória. Quanto maior a string, mais espaço ocupa.
print(getsizeof('Henrique'))

print(getsizeof('Diesel Rodrigues'))
print(getsizeof(1))
print(getsizeof(13))
print(getsizeof(13131313131313))
print(getsizeof(True))

import sys

from sys import getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dict Comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dict Comprehension: {dict_comp} bytes')
print(f'Generator Expression: {gen} bytes')

"""

# Eu posso iterar no Generator Expression? Sim!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)

