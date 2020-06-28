nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

nota = (nota1 + nota2) / 2
reprov = 5.0
aprov = 7.0

if nota >= aprov:
    print(f'\033[32mAprovado!\033[m \033[36mVocê tirou\033[m \033[33m{nota}\033[m')
elif nota < reprov:
    print(f'\033[31mReprovado!\033[m \033[36mVocê tirou\033[m \033[33m{nota}\033[m')
else:
    print(f'\033[35mRecuperação!\033[m \033[36mVocê tirou\033[m \033[33m{nota}\033[m')
