from random import randint
v1 = randint(1, 100)
v2 = randint(1, 100)
v3 = randint(1, 100)
v4 = randint(1, 100)
v5 = randint(1, 100)
valores = (v1, v2, v3, v4, v5)
print(f'Os valores sorteados foram: ', end='')
for n in valores:
    print(f'{n} ', end='')
print(f'\nO numero sorteado maior é {max(valores)}')
print(f'O numero sorteado menor é {min(valores)}')
