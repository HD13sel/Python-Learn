"""
Tipo string

Em Python, um dado é considerado do tipo string sempre em aspas (' " )

nome = 'HD13sel'
print(nome)
print(type(nome))

nome = "Henriq's Bar"
print(nome)
print(type(nome))

nome = 'Henique \nDiesel'  #\n pula de linha
print(nome)
print(type(nome))

nome = "Henrique \" Diesel"
print(nome)
print(type(nome))

# Maiúsculo
nome = 'Henrique Diesel'
print(nome.upper())

# Minúsculo
nome = 'Henrique Diesel'
print(nome.lower())

# Transforma em uma lista de String
nome = 'Henrique Diesel'
print(nome.split())

print(nome[0:8])  # Slice de string

# [     0,        1    ]
# ['Henrique', 'Diesel']
print(nome.split()[1])
"""
# nome = """Henrique
# Diesel"""
# print(nome)
# print(type(nome))

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14  ]
# ['H', 'e', 'n', 'r', 'i', 'q', 'u', 'e', ' ', 'D', 'i', 'e', 's', 'e', 'l' ]
nome = 'Henrique Diesel'
"""
[::-1] => Comece do primeiro elemento, vá até o ultimo elemento e inverter.
"""
print(nome[::-1])  # Inversão de String

print(nome.replace('e', 'y'))  # Trocar letra
print(type(nome))
