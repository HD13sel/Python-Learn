from ex108 import moeda

num = float(input('Digite um valor: R$'))

print(f'Aumentando 10% de {moeda.moeda(num)} é {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'Reduzindo 13% de {moeda.moeda(num)} é {moeda.moeda(moeda.diminuir(num, 13))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')