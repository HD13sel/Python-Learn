"""
Módulo Collections - Counter (Contador)

Collections -> High-Performance Container Datatypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário (dict), contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de
ocorrências desse elemento.

# Realizando o import

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 1, 1, 1, 4, 5, 7, 8, 99, 45, 44, 66, 66, 66]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)

# Coubter ({1: 6, 3: 3, 66: 3, 2: 2, 4: 1, 5: 1, 7: 1, 8: 1, 99: 1, 45: 1, 44: 1})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2

print(Counter('Henrique Diesel'))
# Counter({'e': 4, 'i': 2, 'H': 1, 'n': 1, 'r': 1, 'q': 1, 'u': 1, ' ': 1, 'D': 1, 's': 1, 'l': 1})

"""

from collections import Counter

# Exemplo 3

texto = """Espanha, oficialmente Reino de/da Espanha, é um país principalmente localizado 
na Península Ibérica na Europa. Seu território também inclui dois arquipélagos: as ilhas Canárias, 
na costa da África, e as ilhas Baleares, no mar Mediterrâneo. Os enclaves africanos de Ceuta e Melilla 
fazem da Espanha o único país europeu a ter uma fronteira física com um país africano (Marrocos). 
Várias pequenas ilhas no mar de Alborão também fazem parte do território espanhol. A Espanha continental 
é limitada a sul e a leste pelo Mediterrâneo, exceto por uma pequena fronteira terrestre com Gibraltar; 
a norte e a nordeste pela França, por Andorra e pelo Golfo da Biscaia; e a oeste e noroeste por Portugal 
e pelo Oceano Atlântico. Com uma área de 505 990 quilômetros quadrados, a Espanha é o maior país da Europa 
Meridional, o segundo maior país da Europa Ocidental e da União Europeia (UE) e o quarto maior país de todo 
o continente europeu. Também é o sexto país mais populoso da Europa e o quinto da UE. A capital e maior 
cidade é Madri; outras grandes áreas urbanas incluem Barcelona, Valência, Sevilha, Málaga e Bilbau. """

palavra = texto.split()
# print(palavra)

res = Counter(palavra)
print(res)

# Encontrando as 5 palavras com mais ocorrências no texto
print(res.most_common(5))

