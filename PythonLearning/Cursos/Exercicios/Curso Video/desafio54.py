from datetime import date
anoa = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    anon = int(input(f'Digite o ano de nascimento da {pess}º pessoa: '))
    idade = anoa - anon
    if idade < 21:
        totmenor += 1
    if idade >= 21:
        totmaior += 1
print(f'{totmaior} pessoas são maiores de idade.')
print(f'{totmenor} pessoas são menores de idade.')