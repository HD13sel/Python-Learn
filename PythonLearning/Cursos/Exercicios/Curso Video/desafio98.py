from time import sleep


def contador(i, f, p):
    if i > f and p > 0:
        p = -p

    for v in range(i, f, p):
        print(f'{v} ', end='')
        sleep(0.4)
    print(f, end=' ')
    sleep(0.4)
    print('Fim')
    sleep(0.5)


print('A) 1 até 10 por 1')
contador(1, 10, 1)
print('¨¨'*30)
sleep(2)
print('B) 10 ate 0 por 2')
contador(10, 0, 2)
print('¨¨'*30)
sleep(2)
print('C) Personalizado')
inicio = int(input('Digite o Inicio: '))
fim = int(input('Digite o Fim: '))
passo = int(input('Digite o numero de passos: '))
contador(inicio, fim, passo)
print('¨¨'*30)
