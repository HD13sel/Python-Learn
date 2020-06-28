num = int(input('\033[1;32mDigite um numero qualquer: \033[m'))
escolha = int(input("""\033[1;32mEscolha um numero para conversão:\033[m
\033[32m 1\033[m  ----  \033[7;30mBinário\033[m
\033[32m 2\033[m  ----  \033[7;30mOctal\033[m
\033[32m 3\033[m  ----  \033[7;30mHexadecimal\033[m
 """))
if escolha == 1:
    print(f'\033[33m{num}\033[m = \033[32m{bin(num)[2:]}\033[m')
elif escolha == 2:
    print(f'\033[33m{num}\033[m = \033[35m{oct(num)[2:]}\033[m')
elif escolha == 3:
    print(f'\033[33m{num}\033[m = \033[36m{hex(num)[2:]}\033[m')
else:
    print('\033[31mNumero errado!\033[m \033[1;30mDigite \033[1;32m1 \033[1;30mou \033[1;32m2 \033[1;30mou \033[1;32m3 \033[m')

