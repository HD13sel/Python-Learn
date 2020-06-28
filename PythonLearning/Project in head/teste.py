from random import randint
from time import sleep
contvez = 1
usenum = None
compnum = randint(0, 10)
while usenum != compnum:
    compnum = randint(0, 10)
    print('\n')
    print('\033[35m-=-'*30)
    print('\033[36mEu pensei num numero entre \033[33m0\033[36m a\033[33m 10\033[36m, você consegue adivinhar?')
    print('\033[35m-=-'*30)
    usenum = int(input('\033[32mEm que numero eu pensei? '))  # Jogador tenta adivinhar
    print('\033[36mProcessando..')
    sleep(2)
    if usenum != compnum:
        print('\033[31mComputador ganhou!')
        contvez += 1
    print(f'\033[36mO computador escolheu \033[33m{compnum} \033[36me você escolheu \033[33m{usenum}')

print('\033[32mVocê ganhou!')
print(f'\033[36mVocê tentou \033[33m{contvez} \033[36mvezes')