def numbers(t):
    v = input(f'{t}: ')
    v = int(v)
    for c in range(0, 9999999999):
        if v == c:
            return print(f'{v} é um int')


n = numbers('Digite um numero')
print(f'O {n} é um numero')