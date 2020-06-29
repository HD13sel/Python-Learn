"""
Trabalhando com Módulos Built-in (módulos integrados, que já vem instalados no Python)

# Utilizando alias (apelidos) para módulos/funções

import random as rdm - MODULO
from random import randint as rdi

# Utilizamos (*) para importar todas as funções de um módulo

from random import *

print(randint(x, y))

# Podemos utilizar tuplas para agrupar os imports de um módulo

from random import (
    choice,
    randint,
    uniform,
    shuffle
)
"""