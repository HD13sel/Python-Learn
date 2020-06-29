# mh = 0
# mv = 0
# matrizlist = list()
# for m in range(0, 9):
#     matriznum = int(input(f'Digite um valor para [{mh}, {mv}]: '))
#     mv += 1
#     if mv == 3:
#         mv = 0
#         mh += 1
#     matrizlist.append([matriznum])
# print('-='*30)
# print(f'{matrizlist[ 0 ]}', end=' ')
# print(f'{matrizlist[ 1 ]}', end=' ')
# print(f'{matrizlist[ 2 ]}', end=' ')
# print()
# print(f'{matrizlist[ 3 ]}', end=' ')
# print(f'{matrizlist[ 4 ]}', end=' ')
# print(f'{matrizlist[ 5 ]}', end=' ')
# print()
# print(f'{matrizlist[ 6 ]}', end=' ')
# print(f'{matrizlist[ 7 ]}', end=' ')
# print(f'{matrizlist[ 8 ]}', end=' ')
# print()
# print('-='*30)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
