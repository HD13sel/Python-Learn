num1 = int(input('Digite num1: '))
num2 = int(input('Digite num2: '))
num3 = int(input('Digite num3: '))

# num = [num1, num2, num3]
# print(f'O maximo é {max(num)}')
# print(f'O minimo é {min(num)}')
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print(f'O maior é {maior}')
print(f'O menor é {menor}')
