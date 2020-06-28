"""
# 1 Faça um programa que determine O mostre os cincos primeiro multiplos de 3, considerando numeros maiores que 0
imp = 0
for i in range(1, 18, 1):
    if i % 3 == 0:
        imp += i
        print(f"A soma dos múltiplos ímpares de 3 entre 1 e 5 é {imp}")

# 2 Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes. A primeira deve usar for, dps while e do while
num = 0
for num in (range(1, 101)):
    print(num)
while num in (range(1, 101)):
    print(num)
    break
# 3 Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva na tela, iniciando de 10 em 10 e terminando em 0
from time import sleep
contador = 10
print('Vou estorar em..')
while contador != 0:
    print(f'...{contador}')
    contador = contador - 1
    sleep(1)
print('BUMBUM!!!')
# 4 Escreva um programa que declare um int, incialize com 0 e incremente com 1 em 1, imprimendo seu valor na tela
# até que seu valor chegue a 100;
from time import sleep

contador = 0
print('vo upar minha habildade em python em 100 em...')
while contador != 100:
    print(f'{contador}...')
    contador = contador + 1
    sleep(0.5)
print('so mestre em python agora!')

"""
# 5 faça um programa que peça ao user digitar 10 valores e somar eles
user = int(input('Valor: '))
while user != 10:
    user = user + 1
print(user)
