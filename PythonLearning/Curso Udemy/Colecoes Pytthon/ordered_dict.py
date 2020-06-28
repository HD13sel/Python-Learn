"""
Módulos Collections: Ordered Dict

# Em um dict, a ordem de inserção dos elementos não é garantida.
dicionario = {'a': 1, 'b': 2, 'c': 3}

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')

OrderedDict -> É um dict, que nos garante a ordem de inserção dos elementos.

# Fazenod o import
from collections import OrderedDict

dicionario = OrderedDict({{'a': 1, 'b': 2, 'c': 3}})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

"""
from collections import OrderedDict

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionários comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # True -> Já que ordem dos elementos não importa para o dict.

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # False -> Já que a ordem dos elementos importa para o OrderedDict.
