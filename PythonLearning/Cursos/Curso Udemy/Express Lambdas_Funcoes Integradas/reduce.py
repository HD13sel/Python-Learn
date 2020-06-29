"""
Reduce

OBS: A partir do Python3+ a função reduce() não é mais uma função integrada (built-in). Agora temos que importar e
utilizar esta função a partir do módulo 'funtools'

Guido van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo caso,
99% das vezes um loop for é mais legível.

Para entende o reduce()

# Imagine que você tem uma coleção de daos:

dados = [a1, a2, a3, ..., an]

# # você tem uma função que recebe dois param.:

def funcao(x, y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois param.: a função e o iterável.

reduce(funcao, dados)

A funçõa reduce(), funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiro elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo 1 + o terceiro elemento e guarda o res.

    Isso é repetido até o final.
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn = f(resn, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final,
reduce() irá retornar o resultado final.

Alternativamente, poderíamos vere a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), a4), ...), an)
"""

# Como funciona na prática?

# Vamos utilizar a função reduce() para multiplicar todos os números de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() nós precisamos de uma função que receba dois parâmetros, else TypeError
multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# Utilizando um loop normal

res = 1
for n in dados:
    res = res * n
print(res)

