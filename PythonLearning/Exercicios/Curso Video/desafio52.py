num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print(f'\033[33m{c}', end=' ')
        tot += 1
    else:
        print(f'\033[31m{c}', end= ' ')

print(f'\n\033[34mO número \033[33m{num} \033[34mfoi divisivel \033[33m{tot} \033[34mvezes.')
if tot == 2:
    print('E por isso ele é Primo!')
else:
    print('E por isso ele não é Primo!')
