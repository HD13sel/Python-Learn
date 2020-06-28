from ex109 import moeda

num = float(input('Digite um valor: R$'))

print(f'Aumentando 10% de {moeda.moeda(num)} é {moeda.aumentar(num, 10, True)}')
print(f'Reduzindo 13% de {moeda.moeda(num)} é {moeda.diminuir(num, 13, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')