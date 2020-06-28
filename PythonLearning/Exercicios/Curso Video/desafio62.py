num = int(input('\nDigite o Primeiro número da PA: '))
razao = int(input('Digite a Razão da PA: '))
termo = num
conta = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while conta <= total:
        print(f'{termo}', end=' → ')
        termo += razao
        conta += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais: '))

print('Acabou')