lista = ('Tomate', 3.90, 'Feijão', 2.30, 'Alface', 0.33, 'Repolho', 0.50, 'Bolacha', 2.30, 'Salsicha', 3.40, 'Arroz', 1.89)
print('-'*30)
print(f"{'Supermercadao da Fera':^30}")
print('-'*30)
for pos in range(len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:>4.2f}')
