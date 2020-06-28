from random import randint
cont = 0
while True:

    cnum = randint(0, 10)
    parimpar = str(input('\033[36mEscolha \033[32mPar \033[36mou \033[32mImpar \033[30m[P/I]\033[36m: ')).upper()
    if parimpar in 'P' 'I':
        unum = int(input('\033[36mDigite um numero: '))
        soma = cnum + unum
        resultado = soma % 2

        if resultado == 0:
            print('\033[35m-'*20)
            print(f'\033[36mVocê jogou \033[33m{unum}\033[36m e o computador\033[35m {cnum}\033[36m. Total deu \033[30m{soma}\033[36m e é \033[32mPAR')
            print('\033[35m-' * 20)
            if parimpar == 'P':
                cont += 1
                print('\033[32mVocê venceu!')
                print('\033[36mVamos novamente...')
                print('\033[35m-' * 30)
                continue
            else:
                print('\033[31mVocê perdeu!')
                print('\033[35m-' * 30)
                break
        else:
            print('\033[35m-' * 20)
            print(f'\033[36mVocê jogou \033[33m{unum}\033[36m e o computador\033[35m {cnum}\033[36m. Total deu \033[30m{soma}\033[36m e é \033[32mIMPAR')
            print('\033[35m-' * 20)
            if parimpar == 'I':
                cont += 1
                print('\033[32mVocê venceu!')
                print('\033[36mVamos novamente...')
                print('\033[35m-' * 30)
                continue
            else:
                print('\033[31mVocê perdeu!')
                print('\033[35m-' * 30)
                break

    else:
        print('\033[36mValor incorreto, tente denovo!')
        continue

print('\033[31m#'*30)
print(f'\033[31mGame Over!\033[36m Você venceu\033[33m {cont} \033[36mvezes.')
print('\033[31m#'*30)
