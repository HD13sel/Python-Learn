numext = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    valor = int(input('Digite um numero: '))
    for pos, ext in enumerate(numext):
        if valor == pos:
            print(f'Você digitou o numero {ext}')
            exit()
        if valor > 20 or valor < 0:
            print('Valor incorreto')
            break


