def ficha(nomejog='N/D', numgols=0):
    print(f'O jogador {nomejog} fez {numgols} gol(s) no campeonato.')


jogad = str(input('Nome do jogador: ')).capitalize()
gols = str(input('Numero de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogad.strip() == '':
    ficha(numgols=gols)
else:
    ficha(jogad, gols)

