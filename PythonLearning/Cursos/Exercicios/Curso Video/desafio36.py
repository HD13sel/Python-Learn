casavalor = float(input('Qual o valor da casa? R$'))
salario = float(input('Quanto você ganha? R$'))
anospag = float(input('Quantos anos você deseja pagar? '))

prestacao = casavalor/(anospag * 12)
limite = salario * (30/100)

if prestacao > limite:
    print('\033[31mEmpréstimo negado!\033[m')
    print('\033[31mEstá acima de 30% do seu salário.\033[m')
else:
    print('\033[32mEmprestimo Aprovado!\033[m')
print(f'O valor da prestação vai ser R${prestacao:.2f} durante {anospag:.0f} anos.')