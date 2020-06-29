from ex107 import moeda

num = float(input('Digite um valor: R$'))

print(f'Aumentando 10% de R${num} é R${moeda.aumentar(num, 10)}')
print(f'Reduzindo 13% de R${num} é R${moeda.diminuir(num, 13)}')
print(f'O dobro de R${num} é R${moeda.dobro(num)}')
print(f'A metade de R${num} é R${moeda.metade(num)}')
