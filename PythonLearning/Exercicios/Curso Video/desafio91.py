from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador1': randint(1, 6), 'Jogador2': randint(1, 6), 'Jogador3': randint(1, 6), 'Jogador4': randint(1, 6)}
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('Valores Sorteados:')
sleep(1)
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('Ranking dos Jogadores:')
for k, v in enumerate(ranking):
    print(f'{k+1}º Lugar: {v[0]} tirou {v[1]}')
    sleep(1)


