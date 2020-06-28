# Fatiamento
frase = 'Henrique Diesel Rodrigues'
print(frase[::2])

# Analise
print(len(frase))
print(frase.count('e', 0, 25))
print(frase.find('Die'))
print('Diesel' in frase)

# Transformação
print(frase.replace('Rodrigues', 'Python'))
print(frase.upper())  # Aumenta as letras
print(frase.lower())  # Diminui as letras
print(frase.capitalize())  # Capitaliza a primeira string
print(frase.title())  # Capitaliza todas strings separadas
print(frase.strip())  # Remove espaço vazios entre inicio/fim
print(frase.rstrip())  # Lado direito
print(frase.lstrip())  # Lado esquerdo
print(frase.split())  # Transforma cada string em uma list.
dividido = frase.split()
print(dividido[1])
# Junção
print(' '.join(frase))
print('-'.join(frase))
print('/'.join(frase))
