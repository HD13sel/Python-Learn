"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.


# Biblioteca para trabalhar com dados estatisticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean() << biblioteca statistics
media = statistics.mean(dados)
print(f'Média: {media}')
# OBS: Assim como a função map(), a filter() recebe dois param., sendo uma função e um interável.

res = filter(lambda valor: valor > media, dados)
print(type(res))  # Filter Object
print(list(res))

print(f'Novamente: {list(res)}')

# OBS: Assim como na função map(), após serem utilizados os dados de filter() ele são excluídos da memória.

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)

res = filter(None, paises)  # None filtra os dados vazios e elimina.
print(list(res))

res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

res = filter(lambda pais: pais != '', paises)
print(list(res))


# A diferença entre map() e filter() é:

# map() - Recebe dois param., uma função e um iterável e retona um objeto mapeando a funçao para cada elemento iteravel.
# filter() - Recebe dois param., uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo
com a função.

# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)
# Filtrar os usuários que estão inativos no Twitter

# Forma 1
inativos = list(filter(lambda user: len(user['tweets']) == 0, usuarios))
print(inativos)

# Forma 2
inativos = list(filter(lambda user: not user['tweets'], usuarios))
print(inativos)
"""

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria', 'Jord']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres.

lista = list(map(lambda nome: f'Sua isntrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)

