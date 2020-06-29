def area(larg, comp):
    are = larg * comp
    print(f'A area de {larg}m x {comp}m é {are}m².')


print('¨¨'*30)
print('Calculando a area:')
largu = float(input('Digite a largura: '))
compr = float(input('Digite o comprimento: '))
area(largu, compr)
