soma = 0
total = 0
numuser = int(input('Digite um numero: '))
while numuser != 999:
    soma += numuser
    total += 1
    numuser = int(input('Digite um numero: '))
print(f'Soma: {soma}')
print(f'Digitou {total} numeros')