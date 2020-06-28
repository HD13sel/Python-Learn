from time import sleep

nome = str(input('Digite seu nome: ')).lower()
if nome == 'simoni' or nome == 'simoni diesel' or nome == 'simoni diesel rodrigues':
    print(f'\033[31mFELIZ DIA DAS MÃES! \033[35m{nome.title()}')
    sleep(1)
    print('\033[33mVocê é a melhor mãe do mundo,')
    sleep(1)
    print('\033[33mTe amo!')
    sleep(1)
    print('\033[33mBeijos do seu filho \033[36mHenrique.')
    sleep(1)
else:
    print('\033[31mVocê não é minha mãe.')
