ptermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = ptermo + (10-1) * razao
for c in range(ptermo, decimo + razao, razao):
    print(f'{c}', end=' → ')
print('Acabou')
