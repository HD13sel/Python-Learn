v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))
v4 = int(input('Digite o quarto valor: '))
c = 0
valores = (v1, v2, v3, v4)
print(f'Você digitou os valores: {valores}')

print('A) Valor 9:')
if 9 in valores:
    print(f'Apareceram {valores.count(9)} vezes o valor 9.')
else:
    print('Não temos valores com valor 9.')

print('B) Valor 3:')
if 3 in valores:
    print(f'O numero 3 está na posição {valores.index(3)+1}.')
else:
    print('Não temos valores com valor 3.')
print('C) Pares:')
print('Os numeros pares foram:', end=' ')
for c in valores:
    if c % 2 == 0:
        if c > 0:
            print(f'{c}', end=' ')
