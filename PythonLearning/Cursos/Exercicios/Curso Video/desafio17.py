from math import hypot

co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
hi = hypot(co, ca)
print(f'A hipotenusa é {hi:.2f}')
