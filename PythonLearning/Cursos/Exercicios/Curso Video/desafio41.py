from datetime import date

anonasc = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - anonasc
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 23:
    print('Sênior')
else:
    print('Master')
