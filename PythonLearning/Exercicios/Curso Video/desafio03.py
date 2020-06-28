print('#'*30)
print('Soma de 2 números')
print('\n')
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
confirm = input('Você que saber a soma desses 2 números(S/N)?  ')
if confirm == 'S':
    print(num1 + num2)
    print('Até mais')
if confirm == 'N':
    print('Se você não quer soma, vou fazer subtração!')
    print(num1 - num2)
    print('Até mais')


    
