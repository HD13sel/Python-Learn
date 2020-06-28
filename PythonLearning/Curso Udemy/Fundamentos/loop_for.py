"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Henrique Diesel'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iternado sobre um range)

range(valor_inicial, valor_final)
OBS: o valor final não é inclusive.

for numero in range(1, 10):
    print(numero)

Enumerate:

((0, 'H'), (1, 'e'), (2, 'n'), .....)

for i, v in enumerate(nome):
    print(nome[i])
for indice, letra in enumerate(nome):
    print(letra)
for _, letra in enumerate(nome):
    print(letra)
OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline(_)

nome = 'Henrique Diesel'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)


qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Imprimindo {n}/{qtd} valor:'))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Henrique Diesel'
for letra in nome:
    print(letra, end='')

Tabela de emojis Unicode: https://apps.timhitlock.info/emoji/tables/unicode

"""
# Original: U+1F468
# Modificado: U0001F468

for num in range(1, 11):
    print('\U0001F468' * num)


