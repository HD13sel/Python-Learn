from time import sleep
while True:
    vtab = int(input('Digite qual o valor para mostrar a tabuada: '))
    print('=-=' * 20)

    if vtab < 0:
        break
    else:
        print(f'Tabuada de {vtab}:')
        sleep(1.5)
        for c in range(1, 10 + 1):
            tab = vtab * c
            print(f'{vtab} X {c} = {tab}')
            sleep(0.5)
            c += 1
    print('=-=' * 20)
    sleep(1)

print('Programa encerrado.')
