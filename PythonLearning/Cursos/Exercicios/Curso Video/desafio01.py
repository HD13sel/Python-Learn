#Desafio 1
from time import sleep

pessoa = str(input('\033[0;34mDigite seu nome\033[36m: \033[m'))

print(f'\033[35mOpa\033[37m,\033[35m alguém chegou\033[37m!\033[35m Olá {pessoa}\033[37m,\033[35m seja bem vindo\033[37m!!\033[m')
sleep(2)
print(f'\033[1;33mSee ya \033[7;30m{pessoa}\033[m!!!')

