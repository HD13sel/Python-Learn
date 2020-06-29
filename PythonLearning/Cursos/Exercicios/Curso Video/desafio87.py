mh = 0
mv = 0
matrizlist = list()
pares = list()
tcoluna = list()
slinha = list()
somapares = stcoluna = 0
for m in range(0, 9):
    matriznum = int(input(f'Digite um valor para [{mv}, {mh}]: '))
    if mh == 2:
        tcoluna.append(matriznum)
        stcoluna = sum(tcoluna)
    if mv == 1:
        slinha.append(matriznum)
    mh += 1
    if mh == 3:
        mh = 0
        mv += 1
    matrizlist.append([matriznum])
    if matriznum % 2 == 0:
        pares.append(matriznum)
        somapares = sum(pares)


print('-='*30)
print(f'{matrizlist[ 0 ]}', end=' ')
print(f'{matrizlist[ 1 ]}', end=' ')
print(f'{matrizlist[ 2 ]}', end=' ')
print()
print(f'{matrizlist[ 3 ]}', end=' ')
print(f'{matrizlist[ 4 ]}', end=' ')
print(f'{matrizlist[ 5 ]}', end=' ')
print()
print(f'{matrizlist[ 6 ]}', end=' ')
print(f'{matrizlist[ 7 ]}', end=' ')
print(f'{matrizlist[ 8 ]}', end=' ')
print()
print('-='*30)
print()
print(f'Os pares digitados foram {pares} e a soma deles é {somapares}')
print(f'Os valores da terceira coluna foram {tcoluna} e a soma deles é {stcoluna}')
print(f'Os valores da segunda linha foram {slinha} e o maior valor é {max(slinha)}')