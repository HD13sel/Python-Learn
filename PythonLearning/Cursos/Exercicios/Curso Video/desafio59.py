from time import sleep
numuser = None
nummaior = 0
print('\n')
num1 = int(input('\033[36mDigite o primeiro numero: '))
num2 = int(input('\033[36mDigite o segundo numero: '))
print('\033[35mPreparando o menu...')
sleep(2)
while numuser != 5:
    print('\033[36m-=-'*20)
    print('\033[33m[1]\033[36m Fazer soma')
    print('\033[33m[2]\033[36m Fazer multiplicação')
    print('\033[33m[3]\033[36m Descobrir qual é o maior dos dois números')
    print('\033[33m[4]\033[36m Digitar novos numeros')
    print('\033[33m[5]\033[36m Sair do programa')
    print('\033[36m-=-' * 20)
    numuser = int(input('\033[33mDigite um numero: '))
    if numuser == 1:
        print(f'\033[36mFazer soma de {num1} e {num2}:')
        sleep(0.5)
        print(num1 + num2)
        print('\033[35mPreparando o menu...')
        sleep(2)

    elif numuser == 2:
        print(f'\033[36mFazer multiplicação de {num1} e {num2}:')
        sleep(0.5)
        print(num1 * num2)
        print('\033[35mPreparando o menu...')
        sleep(2)

    elif numuser == 3:
        print(f'\033[36mDescobrindo o maior entre {num1} e {num2}:')
        sleep(0.5)
        if num1 == num2:
            print('Os numeros são iguais.')
            sleep(2)
        elif num1 > num2:
            print(f'\033[33mO {num1} é maior.')
            print('\033[35mPreparando o menu...')
            sleep(2)
        else:
            print(f'\033[33mO {num2} é maior.')
            print('\033[35mPreparando o menu...')
            sleep(2)

    elif numuser == 4:
        print('\033[36mDigite os novos numeros:')
        print('\033[35mUm momento..')
        sleep(1)
        num1 = int(input('\033[36mDigite o primeiro numero: '))
        num2 = int(input('\033[36mDigite o segundo numero: '))
        print('\033[35mPreparando o menu...')
        sleep(2)
    elif numuser == 5:
        print('\033[35mFinalizando...')
        sleep(2)
    else:
        print('\033[36mDigito invalido.')
        print('\033[36mTente novamente.')
        print('\033[35mPreparando o menu...')
        sleep(2)
print('\033[31mVocê saiu do programa.')