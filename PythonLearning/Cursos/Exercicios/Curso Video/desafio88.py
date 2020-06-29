import random
from time import sleep
valorsort = list()
mpl = list()
print('$'*30)
print('Jogo da MEGA SENA')
print('$'*30)
palp = int(input('Quantos palpites deseja? '))
print(f'Sorteando {palp} jogos')
print()
print('$'*30)
for p in range(0, palp):
    for mp in range(0, 61):
        mpl.append(mp)
    valorsort.append(random.sample(mpl, 6))
    print(f'Jogo {p+1}: {valorsort}')
    if len(valorsort) > 0:
        valorsort.pop(0)
    sleep(0.8)
print('$'*30)
print(f"{'BOA SORTE':^30}")
