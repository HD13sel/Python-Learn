"""
Listas (list)

Listas em Python funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dado.

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dados: Não possuem tipo de dados fixos; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Pythons são representadas em colchetes ([]);

As listas são mutáveis: Ou seja, elas podem mudar constantemente.

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 2, 44, 42, 20]

lista2 = ['H', 'D', 'R']

lista3 = []

lista4 = list(range(11))

lista5 = list('HD13sel')

# Pddemos facilmente checar se determinado valor está contido na lista
num = 18
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(4))
print(lista5.count('e'))

# Adicionar elementros em listas

Para adicionar elementos em listas, utilizamos a função append

OBS: Com append, nós só conseguimos adicionar 1 elemento por vez.
# lista1.append(12, 34, 56) #ERRO

print(lista1)
lista1.append(13)
print(lista1)

lista1.append([9, 43, 21])  # Colcoa a lista como elemento único (sublista)
print(lista1)

if [9, 43, 21] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])  # Coloca cada elemento da lista como valor adicional á lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# OBS: Isso não substitui o valor inicial. O mesmo será deslcado para direita na lista.
lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos facilmente juntar duas listas

# lista6 = lista1 + lista2
# lista1.extend(lista2)
# lista1 = lista1 + lista2
print(lista6)

# Podemos facilmente inverter uma lista

# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista

lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro da lista
print(len(lista1))

# Podemos remover facilmente o último elemento de uma lista
# OBS: O pop não somente remove o último elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# OBS: Os elementos á direita deste índice serão deslocados para esquerda.
# OBS: Se não houver elementos no índice informado, teremos o IndexError.
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista
# Exemplo 1
# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas.
curso = 'Programação em Python'
print(curso)
curso = curso.split()
print(curso)

# Exemplo 2
curso = 'Programação,em,Python'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string

lista6 = ['Programação', 'em', 'Python']
print(lista6)

# Abaixo: Pega a lista 6, coloca espaço entre cada elemento e transforma em uma string.
curso = ' '.join(lista6)
print(curso)
# Abaixo: Pega a lista 6, coloca cifrão($) entre cada elemento e transforma em uma string.
curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

lista6 = [1, 2.34, True, 'HDR', 'd', [1, 2, 3], 4545449454]
print(lista6)
print(type(lista6))

# Iterando sobre listas

# Exemplo 1 (Utilizando for)
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 (Utilizando while)
carrinho = []
produto = ''
while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

cores = ['verde', 'amarelo', 'azul', 'branco']

# Fazemos acesso aos elementos de forma indexada
#           0          1       2         3
cores = ['verde', 'amarelo', 'azul', 'branco']
#          -4         -3      -2        -1

print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# Fazer acesso aos elementos de forma indexada inversa
# Pàra entender melhor o índice negativo, pense na lista como um círculo, onde
# o final de um elemento está ligado ao ínicio da lista
print(cores[-4])  # verde
print(cores[-3])  # amarelo
print(cores[-2])  # azul
print(cores[-1])  # branco

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos
lista = []
lista.append(13)
lista.append(13)
lista.append(13)
lista.append(13)
print(lista)

# Outros métodos não tão importantes mas também úteis

# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual indice está o valor (6)
print(numeros.index(6))

# Em qual indice está o valor (9)
print(numeros.index(9))

# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError
# print(numeros.index(19))

# OBS: Retorna o índice do primeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
print(numeros.index(5, 1))  # Buscando a partir do índice 1
# print(numeros.index(5, 4))  # Buscando a partir do índice 4 (ValueError)

# Podemos fazer busca dentro de um range, ínicio/fim
print(numeros.index(8, 3, 8))  # Buscar o índice do valor 8, entre os índices 3 a 8

# Revisão de slicing

# lista[ínicio:fim:passo]
# range[íncio:fim:passo]

lista = [1, 2, 3, 4]

# Trabalhando com slice de lista com o parâmetro 'ínicio'

print(lista[1:])  # Iniciando no índice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parâmetro 'fim'

print(lista[:2])  # começa em 0, pega até o índice 2 - 1 (inclusive)

# Trabalhando com slice de lista com o parâmetro 'passo'

print(lista[1::2])  # começa em 1, vai até o final, e vai em passo de 2 em 2.

# Invertendo valores em uma lista

nomes = ['Henrique', 'Diesel']

nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['Henrique', 'Diesel']
nomes.reverse()
print(nomes)

# Soma*, Valor Max*, Valor Min*, Tamanho

# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))  # Soma
print(max(lista))  # Valor Max
print(min(lista))  # Valor Min
print(len(lista))  # Tamanho

# Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))


# Desempacotamento de listas

# OBS: Se tivermos um número diferente de elementos na lista ou varáveis para receber os dados, teremos ValueError;
lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 (Deep Copy)
lista = [1, 2, 3]
print(lista)

nova = lista.copy()  # cópia
print(nova)

nova.append(4)

print(lista)
print(nova)
# Veja que ao utilizarmos "lista.copy()" copiamos os dados da lista para uma nova lista, mas elas
# ficaram totalmente independentes, ou seja, modificando uma lista, não afeta outra. Isso em Python
# é chamado de Deep Copy (cópia profunda)

# Forma 2 (Shallow Copy)
lista = [1, 2, 3]
print(lista)

nova = lista  # cópia
print(nova)

nova.append(4)

print(lista)
print(nova)
# Veja que ao utilizarmos "nova = lista", copiamos os dados da lista para a nova lista, mas
# após realizar modificação em uma das listas, esssa modificação se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy.
"""


