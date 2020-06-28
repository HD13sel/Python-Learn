numuser = int(input('Digite um numero: '))
c = numuser
f = 1
print(f'Calculando {numuser}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *=c
    c -= 1

print(f'{f}.')


