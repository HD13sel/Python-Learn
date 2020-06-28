temp = list()
grupo = list()
perg = ''
pesmai = list()
pesmenor = list()
mai = men = 0
while perg != 'n':
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(grupo) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    grupo.append(temp[:])
    temp.clear()
    perg = str(input('Quer continuar [s/n]: ')).lower()
print('-='*30)
print(f'O numero de pessoas registradas foram: {len(grupo)}')
print(f'O maior peso foi de {mai}Kg. Peso de', end=' ')
for p in grupo:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de', end=' ')
for p in grupo:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')

