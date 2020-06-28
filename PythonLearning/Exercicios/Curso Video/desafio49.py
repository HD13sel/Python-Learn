from time import sleep
num = int(input('Digite um número: '))
print(f'A tábuada de {num}:')
for x in range(0, 10+1):
    print(f'{num} x {x} = {num*x}')
    sleep(0.15)
