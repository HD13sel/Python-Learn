lisgols = []
nome = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas o {nome} jogou? '))
for c in range(1, partidas+1):
    gols = int(input(f'Quantos gols na partida {c}? '))
    lisgols.append(gols)
dados = {'Nome': nome, 'Gols': lisgols, 'total': sum(lisgols)}
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {nome} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'=> Na partida {c+1}, fez {lisgols[c]} gols.')
print(f'Foi um total de {sum(lisgols)} gols.')
