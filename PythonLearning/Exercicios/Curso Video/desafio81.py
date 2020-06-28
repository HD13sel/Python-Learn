valores = []
perg = ''
while perg != 'n':
    valores.append(int(input('Digite um valor: ')))
    perg = str(input('Quer continuar [s/n]: ')).lower()
print(f'Foram {len(valores)} numeros digitados')
valores.sort(reverse=True)
print(valores)
if 5 in valores:
    print(f'Temos o 5, {valores.count(5)}x nos valores')
else:
    print('Não temos 5 nos valores')