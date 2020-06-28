"""
Min e Max

max() -> Retorna o valor máximo em um iterável ou o maior de dois ou mais elementos.

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))  # 129

tupla = 1, 8, 4, 99, 34, 129
print(max(tupla))  # 129

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))  # 129

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario))  # f
print(max(dicionario.values()))  # 129

# Faça um programa que receba 2 valores do user e mostre o maior:

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(max(val1, val2))

print(max(4.3, 5.47033, 0.5408))
print(max('a', 'ab', 'abc'))
print(max('a', 'b', 'c', 'g'))
print(max('Henrique Diesel'))


min() -> Retorna o valor mínimo em um iterável ou o menor de dois ou mais elementos.


# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))  # 1

tupla = 1, 8, 4, 99, 34, 129
print(min(tupla))  # 1

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))  # 1

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario))  # a
print(min(dicionario.values()))  # 1

# Faça um programa que receba 2 valores do user e mostre o maior:

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(min(val1, val2))

print(min(4.3, 5.47033, 0.5408))
print(min('a', 'ab', 'abc'))
print(min('a', 'b', 'c', 'g'))
print(min('Henrique Diesel'))

# Outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Olivander']

print(max(nomes))  # Tim
print(min(nomes))  # Arya

print(max(nomes, key=lambda nome: len(nome)))  # Ollivander
print(min(nomes, key=lambda nome: len(nome)))  # Tim
"""

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 3},
    {"titulo": "Too old to rock'in'roll, too  young to die", "tocou": 32},
]
# print(max(musicas))  # TypeError

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO! Imprima somente o título da musica mais e menos tocada.

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# DESAFIO! Como encontrar a música mais tocada e a menos tocada sem usar max(), min(), lambda?
max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']
        print(max)

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 9999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']
        print(min)

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])


