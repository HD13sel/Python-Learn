from time import sleep

produtos = {10419: 'Call of Duty: Modern Warfare', 11319: 'Ghost Recon: Breakpoint', 12320: 'Cyberpunk 2077'}
codigos = {1: 10419, 2: 11319, 3: 12320}
p1 = codigos[1]
p2 = codigos[2]
p3 = codigos[3]
vp1 = 135.50
vp2 = 95.50
vp3 = 249.50

print('-=-' * 20)
print('Escolha seu jogo:')
sleep(0.5)
print(f'#{p1} ---- {produtos[p1]} --- R${vp1} ')
sleep(0.5)
print(f'#{p2} ---- {produtos[p2]} --- R${vp2}')
sleep(0.5)
print(f'#{p3} ---- {produtos[p3]} --- R${vp3}')
sleep(0.5)
print('-=-' * 20)
sleep(2)
escolhauser = int(input('Escreva o código do produto: #'))
print(f'Processando... ')
sleep(3)

if escolhauser == p1:
    print(f'O código é #{escolhauser} e o produto é {produtos[p1]} e seu valor é R${vp1}')
    sleep(3)
    confirmuser = str(input(f'Deseja confirmar a compra do jogo {produtos[p1]}: ')).lower()
    if confirmuser == 'yes' or confirmuser == 'sim' or confirmuser == 'ok':
        print('Qual tipo de pagamento você prefere? ')
        sleep(1)
        vista = str(input('À vista, dinheiro ou cheque? (10% de desconto)  ')).lower()
        if vista == 'yes' or vista == 'sim' or vista == 'ok':
            print(f'O valor é R${vp1 - (vp1 * 10 / 100)}.')
            sleep(2)
            exit('Compra efetuada!')
        cartaov = str(input('À vista no cartão de crédito? (5% de desconto)  ')).lower()
        if cartaov == 'yes' or cartaov == 'sim' or cartaov == 'ok':
            print(f'O valor é R${vp1 - (vp1 * 5 / 100)}.')
            sleep(2)
            exit('Compra efetuada!')
        cartao2p = input('Em até 2x no cartão de crédito? (Sem juros)  ')
        if cartao2p == 'yes' or cartao2p == 'sim' or cartao2p == 'ok':
            print(f'O valor é R${vp1 / 2} em 2x.')
            sleep(2)
            exit('Compra efetuada!')
        cartaop = input('Parcelar no cartão 3x ou mais? (20% juros)  ')
        if cartaop == 'yes' or cartaop == 'sim' or cartaop == 'ok':
            parc = int(input('Quantas vezes você deseja pagar (3 a 5): '))
            if parc == 3:
                print(f'O valor é R${(((vp1 / 3) * 20 / 100) + (vp1 / 3))} em 3x.')
                sleep(2)
                exit('Compra efetuada')
            elif parc == 4:
                print(f'O valor é R${(((vp1 / 4) * 20 / 100) + (vp1 / 4))} em 4x.')
                sleep(2)
                exit('Compra efetuada')
            elif parc == 5:
                print(f'O valor é R${(((vp1 / 5) * 20 / 100) + (vp1 / 5))} em 5x.')
                sleep(2)
                exit('Compra efetuada')
            else:
                print('Número de parcelas indisponíveis.')
                sleep(2)
                exit()
    else:
        print('Você não confirmou!')
        sleep(2)
        exit()
elif escolhauser == p2:
    print(f'O código é #{escolhauser} e o produto é {produtos[p2]} e seu valor é R${vp2}')
    sleep(3)
    confirmuser = str(input(f'Deseja confirmar a compra do jogo {produtos[p2]}: ')).lower()
    if confirmuser == 'yes' or confirmuser == 'sim' or confirmuser == 'ok':
        print('Qual tipo de pagamento você prefere? ')
        sleep(1)
        vista = str(input('À vista, dinheiro ou cheque? (10% de desconto)  ')).lower()
        if vista == 'yes' or vista == 'sim' or vista == 'ok':
            print(f'O valor é R${vp2 - (vp2 * 10 / 100)}.')
            sleep(2)
            exit('Compra efetuada!')
        cartaov = str(input('À vista no cartão de crédito? (5% de desconto)  ')).lower()
        if cartaov == 'yes' or cartaov == 'sim' or cartaov == 'ok':
            print(f'O valor é R${vp2 - (vp2 * 5 / 100)}.')
            sleep(2)
            exit('Compra efetuada!')
        cartao2p = input('Em até 2x no cartão de crédito? (Sem juros)  ')
        if cartao2p == 'yes' or cartao2p == 'sim' or cartao2p == 'ok':
            print(f'O valor é R${vp2 / 2} em 2x.')
            sleep(2)
            exit('Compra efetuada!')
        cartaop = input('Parcelar no cartão 3x ou mais? (20% juros)  ')
        if cartaop == 'yes' or cartaop == 'sim' or cartaop == 'ok':
            parc = int(input('Quantas vezes você deseja pagar (3 a 5): '))
            if parc == 3:
                print(f'O valor é R${(((vp2 / 3) * 20 / 100) + (vp2 / 3))} em 3x.')
                sleep(2)
                exit('Compra efetuada')
            elif parc == 4:
                print(f'O valor é R${(((vp2 / 4) * 20 / 100) + (vp2 / 4))} em 4x.')
                sleep(2)
                exit('Compra efetuada')
            elif parc == 5:
                print(f'O valor é R${(((vp2 / 5) * 20 / 100) + (vp2 / 5))} em 5x.')
                sleep(2)
                exit('Compra efetuada')
            else:
                print('Número de parcelas indisponíveis.')
                sleep(2)
                exit()

    else:
        print('Você não confirmou!')
        sleep(2)
        exit()
elif escolhauser == p3:
    print(f'O código é #{escolhauser} e o produto é {produtos[p3]} e seu valor é R${vp3}')
    sleep(3)
    confirmuser = str(input(f'Deseja confirmar a compra do jogo {produtos[p3]}: ')).lower()
    if confirmuser == 'yes' or confirmuser == 'sim' or confirmuser == 'ok':
        print('Qual tipo de pagamento você prefere? ')
        sleep(1)
        vista = str(input('À vista, dinheiro ou cheque? (10% de desconto)  ')).lower()
        if vista == 'yes' or vista == 'sim' or vista == 'ok':
            print(f'O valor é R${vp3 - (vp3 * 10 / 100)}.')
            sleep(2)
            exit('Compra efetuada!')
        cartaov = str(input('À vista no cartão de crédito? (5% de desconto)  ')).lower()
        if cartaov == 'yes' or cartaov == 'sim' or cartaov == 'ok':
            print(f'O valor é R${vp3 - (vp3 * 5 / 100)}.')
            sleep(2)
            exit('Compra efetuada!')
        cartao2p = input('Em até 2x no cartão de crédito? (Sem juros)  ')
        if cartao2p == 'yes' or cartao2p == 'sim' or cartao2p == 'ok':
            print(f'O valor é R${vp3 / 2} em 2x.')
            sleep(2)
            exit('Compra efetuada!')
        cartaop = input('Parcelar no cartão 3x ou mais? (20% juros)  ')
        if cartaop == 'yes' or cartaop == 'sim' or cartaop == 'ok':
            parc = int(input('Quantas vezes você deseja pagar (3 a 5): '))
            if parc == 3:
                print(f'O valor é R${(((vp3 / 3) * 20 / 100) + (vp3 / 3))} em 3x.')
                sleep(2)
                exit('Compra efetuada')
            elif parc == 4:
                print(f'O valor é R${(((vp3 / 4) * 20 / 100) + (vp3 / 4))} em 4x.')
                sleep(2)
                exit('Compra efetuada')
            elif parc == 5:
                print(f'O valor é R${(((vp3 / 5) * 20 / 100) + (vp3 / 5))} em 5x.')
                sleep(2)
                exit('Compra efetuada')
            else:
                print('Número de parcelas indisponíveis.')
                sleep(2)
                exit()
    else:
        print('Você não confirmou!')
        sleep(2)
        exit()
else:
    print(f'Código #{escolhauser} não existe.')
    sleep(2)

