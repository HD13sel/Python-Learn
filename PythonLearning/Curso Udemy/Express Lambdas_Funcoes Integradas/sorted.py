"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em Listas. O sort() só funciona em Listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o própio nome diz, sorted() serve par ordenar.

OBS: O sorted() SEMPRE retorna uma list com os elementos do iterável ordenados.

# Exemplo

numeros = {6, 1, 8, 2}
print(numeros)

print(sorted(numeros))  # Ordenar do menor para o maior.
print(numeros)

# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True))  # Ordena do maior para o menor.

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]

print(usuarios)

# Ordenando pelo username - Ordem Alfabetica
print(sorted(usuarios, key=lambda user: user["username"]))

# Ordenando pelo número tweets
print(sorted(usuarios, key=lambda user: len(user["tweets"])))

"""

# Ultimo exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 3},
    {"titulo": "Too old to rock'in'roll, too  young to die", "tocou": 32},
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))






