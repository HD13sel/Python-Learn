n = int(input('Digite um numero: '))
f = 1
print(f'{n}! = ', end='')
for c in range(n, f-1, -1):
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')