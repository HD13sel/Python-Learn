valores = []
maxi = 0
mini = 0
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if cont == 0:
        maxi = valores[cont]
        mini = valores[cont]
    else:
        if valores[cont] > maxi:
            maxi = valores[cont]
        if valores[cont] < mini:
            mini = valores[cont]

print('||-'*30)
print(f'A lista é: {valores}')
print(f'O elemento maximo é: {maxi} e está na posicao ', end='')
for i, v in enumerate(valores):
    if v == maxi:
        print(f'{i}...', end='')
print()
print(f'O elemento minimo é: {mini} e está na posicao ', end='')
for i, v in enumerate(valores):
    if v == mini:
        print(f'{i}...', end='')
print()