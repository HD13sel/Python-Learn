from random import randint
from time import sleep
compnum = randint(0, 5)  # Computador "PENSA"
print('-=-'*30)
print('Eu pensei num numero entre 0 a 5, você consegue adivinhar?')
print('-=-'*30)
usenum = int(input('Em que numero eu pensei? '))  # Jogador tenta adivinhar
print('Processando..')
sleep(2)
if usenum == compnum:
    print('Ahh, você leu meus pensamentos, você ganhou!')
else:
    print('Ganhei, você não disse o número que pensei!')
print(f'O computador escolheu {compnum} e você escolheu {usenum}')

