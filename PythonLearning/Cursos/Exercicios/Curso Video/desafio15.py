diasalug = int(input('Quantos dias alugados? '))
kmrod = float(input('Quantos Km rodados? '))

preco = (diasalug * 60) + (kmrod * 0.15)
print(f'O total a pagar é de R${preco}')
