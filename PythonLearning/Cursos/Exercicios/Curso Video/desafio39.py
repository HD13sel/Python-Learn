from datetime import date
anonasc = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - anonasc
alistidade = 18

if idade < alistidade:
    print(f'Você tem {idade} anos e vai poder se alistar quando tiver {alistidade} anos')
    print(f'Falta apenas {alistidade - idade} anos para poder se alistar')
elif idade > alistidade:
    print(f'Você tem {idade} anos e passou o tempo do alistamento')
    print(f'Já passou {idade - alistidade} anos após o alistamento')
else:
    print(f'Você tem {idade} anos e está na hora de se alistar! Salve a pátria!')
