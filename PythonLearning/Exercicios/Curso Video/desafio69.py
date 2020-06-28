ch = cm = idc = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Qual o sexo [M/F]: ')).upper()
    if sexo in 'M' 'F':
        if idade > 18:
            idc += 1
        if sexo == 'M':
            ch += 1
        if sexo == 'F':
            if idade < 20:
                cm += 1
    else:
        print('Digito errado, tente novamente.')
        continue
    userd = str(input('Quer continuar [S/N]: ')).upper()
    if userd in 'S':
        print('Armazenando...')
    else:
        print('Encerrando..')
        break
print(f'Tem {idc} maiores de 18 anos.')
print(f'Tem {ch} homens.')
print(f'Tem {cm} mulheres abaixo de 20 anos.')