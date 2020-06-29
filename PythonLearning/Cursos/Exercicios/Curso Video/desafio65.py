soma = 0
total = 0
maiornum = 0
menornum = 0
respuser = ''
while respuser != 'N':
    num = int(input('Digite um valor: '))
    total = total + 1
    soma += num
    if num > maiornum:
        maiornum = num
    if menornum == 0:
        menornum = num
    if num < menornum:
        menornum = num

    respuser = str(input('Digite [S] para continuar ou [N] para sair: ')).upper()
    if respuser != 'S' and respuser != 'N':
        exit('Digito errado')
print(f'Você digitou {total} e a media é {soma / total}')
print(f'O menor valor é {menornum}')
print(f'O maior valor é {maiornum}')
