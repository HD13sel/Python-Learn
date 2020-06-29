sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).upper()
if sexo == 'M':
    print('Masculino')
if sexo == 'F':
    print('Feminino')
