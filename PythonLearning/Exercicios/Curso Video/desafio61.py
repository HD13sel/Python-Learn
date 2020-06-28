num = int(input('\nDigite o Primeiro número da PA: '))
razao = int(input('Digite a Razão da PA: '))
decimo = num + (10-1) * razao
termo = num
conta = 1
decrazao = decimo + razao
while conta <= 10:
    print(f'{termo}', end=' → ')
    termo += razao
    conta += 1
print('Acabou')