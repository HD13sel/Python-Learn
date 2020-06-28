def maior(*num):
    print('Os numeros foram:')
    print(*num)
    print(f'O maior numero é {max(*num)}')
    print(f'O total de numeros foram {len(*num)}')


numel = list()
while True:
    nume = int(input('Digite um numero: '))
    numel.append(nume)
    while True:
        perg = str(input('Quer continuar [s/n]: ')).lower()
        if perg in 'sn':
            break
        print('Erro! Digite apenas [s/n]')
    if perg == 'n':
        break
maior(numel)

