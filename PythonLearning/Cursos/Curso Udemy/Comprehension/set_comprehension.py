"""
Set Comprehension

Lista = [1, 2, 3]
Set = {1, 2, 3}

Sintaxe:
{valor for valor in iterável}

"""

# Exemplos

numeros = {num for num in range(1, 7)}
print(numeros)

# Outro exemplo

numeros = {x ** 2 for x in range(10)}
print(numeros)

# Faça uma alteração na estrutura acima para gerar um dict ao invés do set

numeros = {x: x * 2 for x in range(10)}
print(numeros)

# Para finalizar

letras = {letra for letra in 'Henrique Diesel'}
print(letras)

