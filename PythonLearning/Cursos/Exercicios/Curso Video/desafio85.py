valores = list()
pares = list()
impares = list()
for v in range(0, 7):
    valor = int(input(f'Digite o {v+1}º valor: '))
    if valor % 2 == 0:
        pares.append(valor)
        pares.sort()
    else:
        impares.append(valor)
        impares.sort()
valores.append(pares)
valores.append(impares)
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores impares digitados foram: {valores[1]}')
