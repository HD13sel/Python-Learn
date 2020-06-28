listageral = []
listapar = []
listaimpar = []
perg = ' '
while perg != 'n':
    listageral.append(int(input('Digite um valor: ')))
    perg = str(input('Quer continuar [s/n]: ')).lower()
for v in listageral:
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)
print('#'*30)
print(f'Os numeros da lista foram: {listageral}')
print('#'*30)
print(f'Os numeros par são: {listapar}')
print('#'*30)
print(f'Os numeros impar são: {listaimpar}')
