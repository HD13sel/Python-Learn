from random import choice
comp = {0: 'Pedra', 1: 'Papel', 2: 'Papel'}
# 0 - Papel, 1 - Pedra, 2- Tesoura
esc = choice(comp)
usernum = str(input('Escolha um (Pedra, Papel, Tesoura): '))

if usernum == esc:
    print('Empate')
if usernum == 'Pedra':
    if esc == 'Tesoura':
        print('Você ganhou')
    if esc == 'Papel':
        print('Computador ganhou')
if usernum == 'Papel':
    if esc == 'Tesoura':
        print('Computador ganhou')
    if esc == 'Pedra':
        print('Você ganhou')
if usernum == 'Tesoura':
    if esc == 'Papel':
        print('Voce ganhou')
    if esc == 'Pedra':
        print('Computador ganhou')
print(f'Você escolheu {usernum} e o computador escolheu {esc}')