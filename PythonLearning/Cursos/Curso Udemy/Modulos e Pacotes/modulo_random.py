"""

Módulo Random

- Em Python, módulos nada mais são do que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatórios.

# OBS: Existem 2 formas de se utilizar um módulo ou função deste

# Forma 1 # Importando todo o módulo (Não recomendado)
import random

##############
# random() -> Gera um número real pseudo-aleatório entre 0 e 1.
##############

# Ao realizar import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do módulo ficarão disponíveis. (Ficarão em memória). Caso você saiba quais funções você precisa utilizar
# deste módulo, então esta não seria a forma ideal de utilização. Nós veremos um forma melhor na forma 2.

print(random.random())

# Veja que p/ utilizar a função random() do módulo random, nós colocamos o nome do módulo e o nome da função,
# separados por (.).

# OBS: Não confunda a função random() com o módulo random. Pode parecer confuso, mas a função random() é uma função
# dentro do módulo random.


# Forma 2 - 0 Importando uma função específica do módulo (Forma recomendada)

from random import random

# No import acima, estamos falando: Do módulo random, importe a função random.

for i in range(10):
    print(random())

###############
# uniform() -> Gera um número real pseudo aleatório entre os valores estabelecidos
###############

from random import uniform

for i in range(10):
    print(uniform(5, 10))  # 10 não é incluído.

###############
# randint() -> Gera valores inteiros pseudo-aleatórios entre os valores estabelecidos.
###############

from random import randint

# Gerador de apostas para mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')  # Começa em 1 e vai até 60

##############
# choice() -> Mostra um valor aleatório entre um iterável.
##############

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

###############
# shuffle() -> Tem a função de embaralhar dados
###############

from random import shuffle

cartas = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']

print(cartas)
shuffle(cartas)
print(cartas)
"""




