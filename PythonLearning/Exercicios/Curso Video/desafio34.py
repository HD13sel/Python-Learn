salario = float(input('Digite seu salario: '))
superior = (salario*10/100)+salario
inferior = (salario*15/100)+salario

if salario <= 1250:
    print(f'Seu aumento ficou com R${inferior:.2f}')
else:
    print(f'Seu aumento ficou com R${superior:.2f}')