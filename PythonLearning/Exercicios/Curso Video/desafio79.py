valores = []
perg = ''
while perg != 'n':
    num = int(input('Digite um valor: '))
    if num in valores:
        print('Esse numero ja existe!')

    else:
        valores.append(num)
        print('Valor adicionado.')

    perg = input(str('Quer continuar? [S/N] ')).lower()
print(sorted(valores))