def escreva(txt):
    tam = len(txt)+4
    print('='*tam)
    print(f'  {txt}')
    print('='*tam)


user = str(input('Digite a frase: '))
escreva(user)