print('-'*20)
print('Banco HCode')
print('-'*20)
saque = int(input('Digite o valor do saque: R$'))
ced50 = 50
ced20 = 20
ced10 = 10
ced5 = 5
ced = 1
tced50 = tced20 = tced10 = tced5 = tced = 0
while True:
    if saque >= 50:
        saque -= ced50
        tced50 += 1
        if saque == 0:
            break
    elif saque >= 20:
        saque -= ced20
        tced20 += 1
        if saque == 0:
            break
    elif saque >= 10:
        saque -= ced10
        tced10 += 1
        if saque == 0:
            break
    elif saque >= 5:
        saque -= ced5
        tced5 += 1
        if saque == 0:
            break
    elif saque >= 1:
        saque -= ced
        tced += 1
        if saque == 0:
            break
    else:
        print('valor incorreto')

print(f'O total das cedulas foi:')
if tced50 > 0:
    print(f'Cedulas de R$50: {tced50}')
if tced20 > 0:
    print(f'Cedulas de R$20 = {tced20}')
if tced10 > 0:
    print(f'Cedulas de R$10 = {tced10}')
if tced5 > 0:
    print(f'Cedulas de R$5 = {tced5}')
if tced > 0:
    print(f'Cedulas de R$1 = {tced}')