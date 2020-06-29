"""
Tipo float

Tipo real, decimal

Casas decimais

OBS: O separador de casas decimais na programação é o "." e não ",";
"""
# Errado do ponto de vista do Float, mas gera "tuple"
valor = 1,44  # "tuple"
print(type(valor))
# Certo do ponto de vista do Float
valor = 1.44  # "float"
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1,44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos convert um float para int
"""
OBS: Ao converter valores float para inteiros, perdemos precisão.
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j
print(type(variavel))

