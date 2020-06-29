from random import randint
from time import sleep
numer = list()
numerpar = list()


def linha():
    print('¨¨'*30)


def sorteia5(i, f):
    for c in range(0, 5):
        n = randint(i, f)
        print(n, end=' ')
        sleep(1)
        numer.append(n)
    print()
    linha()
    print(f'A lista dos numeros sorteados: {numer}')
    sleep(1)


def somapar(lst):
    for c, v in enumerate(lst):
        if v % 2 == 0:
            numerpar.append(v)
    linha()
    print(f'Os numeros pares de {numer} são {numerpar}')
    sleep(1)
    linha()
    print(f'A soma dos numeros pares é {sum(numerpar)}')
    sleep(1)


linha()
print('Sorteando 5 numeros!')
linha()
inicio = int(input('Digite o valor inicial para o sorteio: '))
final = int(input('Digite o valor final para o sorteio: '))
print('Os numeros sorteados foram:', end=' ')
sorteia5(inicio, final)
somapar(numer)
