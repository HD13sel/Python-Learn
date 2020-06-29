from time import sleep
s = pmil = nmenor = menor = 0
while True:
    nprod = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    s += preco
    if menor == 0:
        menor = preco
    if preco > 1000:
        pmil += 1
    if preco < menor:
        menor = preco
    if menor == preco:
        nmenor = nprod
    userd = ' '
    while userd not in 'SN':
        userd = str(input('Deseja adicionar mais produtos? [S/N]: ')).upper()

    if userd == 'N':
        print('Compra encerrada.')
        break
    print('Colocando no carrinho..')
    sleep(1.0)


print('-'*20)
print(f'Total da compra foi R${s:.2f}')
print(f'Você comprou {pmil} produtos acima de R$1000')
print(f'O produto mais barato do carrinho foi {nmenor}, apenas R${menor}')
print('-'*20)