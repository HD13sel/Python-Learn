from math import radians, sin, cos, tan
angul = float(input('Digite um angulo: '))
seno = sin(radians(angul))
cosse = cos(radians(angul))
tange = tan(radians(angul))
print(f'O seno é {seno:.2f}')
print(f'O cosseno é {cosse:.2f}')
print(f'O tangente é {tange:.2f}')
