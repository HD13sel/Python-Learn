pesomenor = 0
pesomaior = 0
for pess in range(1, 6):
    peso = float(input(f'Digite o peso da {pess}º pessoa: '))
    if pess == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print(f'O maior peso lido foi de {pesomaior}kg.')
print(f'O menor peso lido foi de {pesomenor}kg.')
