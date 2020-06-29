from time import sleep

nomec = str(input('Nome completo? ')).strip()
print('Analisando seu nome...')
sleep(2)
print(f'Seu nome em maiúsculas {nomec.upper()}')
sleep(1)
print(f'Seu nome em minúsculas {nomec.lower()}')
sleep(1)
print(f'Seu nome tem {len(nomec) - nomec.count(" ")} letras')
sleep(1)
print(f'Seu primeiro nome tem {nomec.find(" ")} letras')
