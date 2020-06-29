media = 0
sexo = ''
totidade = 0
idademaior = 0
nomevelho = ''
totm = 0
sexov = ''

for p in range(1, 5):
    print('-=-'*20)
    print(f'{p} Pessoa')
    print('-=-'*20)
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: ')).lower()
    if sexo == 'm' or sexo == 'masculino' or sexo == 'homem':
        sexo = 'Masculino'
    elif sexo == 'f' or sexo == 'feminino' or sexo == 'mulher':
        sexo = 'Feminino'
        if idade < 20:
            totm += 1
    elif sexo == 'outro' or sexo == 'nao revelado':
        sexo = 'Outro'
    else:
        print('Inválido')
        print('Tente novamente')
        exit('Encerrado')

    totidade += idade
    if idade > idademaior:
        idademaior = idade
    if idademaior == idade:
        nomevelho = nome
        sexov = sexo

    media = totidade / p

# Mostrando media
print(f'\nA média do grupo é {media:.2f} anos')

# Mostrando pessoa mais velha
if sexov == 'Masculino':
    print(f'{nomevelho} é o mais velho com {idademaior} anos.')
if sexov == 'Feminino':
    print(f'{nomevelho} é a mais velha com {idademaior} anos.')
if sexov == 'Outro':
    print(f'{nomevelho} é o(a) mais velho(a) com {idademaior} anos.')

# Mostrando mulheres abaixo de 20 anos
if totm == 0:
    print('Não tem mulheres abaixo de 20 anos')
elif totm == 1:
    print(f'Tem {totm} mulher abaixo de 20 anos')
else:
    print(f'São {totm} mulheres abaixo de 20 anos')