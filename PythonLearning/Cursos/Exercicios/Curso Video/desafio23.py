num = int(input('Informe um numero: '))
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000 % 10
print(f'Analisando o numero {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')



# numero = str(input('Digite um numero entre 0-9999: '))
# print(f'Milhar: {numero[0]}')
# print(f'Centena: {numero[1]}')
# print(f'Dezena: {numero[2]}')
# print(f'Unidade: {numero[3]}')