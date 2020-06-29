perg = ''
mediai = 0
pessoa = dict()
lispmaisqmedia = list()
lispessoa = list()
lisidades = list()
lispidades = list()
lismul = list()
while True:
    nome = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo [M/F]: ')).upper()
        if sexo in 'MF':
            break
        print('Erro! Digite apenas M/F!')
    idade = int(input('Idade: '))
    pessoa = {'Nome': nome, 'Sexo': sexo, 'Idade': idade}
    if sexo == 'F':
        lismul.append(nome[:])
    dpidades = {'nome': nome, 'ida': idade}
    lispidades.append(dpidades.copy())
    lisidades.append(idade)
    lispessoa.append(pessoa.copy())
    while True:
        perg = str(input('Deseja cadastrar mais uma pessoa? [s/n] ')).upper()
        if perg in 'SN':
            break
        print('Erro! Digite apenas S/N!')
    if perg == 'N':
        break
print('¨'*30)
print(f'Foram cadastradas {len(lispessoa)} pessoas')
for i in lisidades:
    somai = sum(lisidades)
    mediai = somai / len(lisidades)
print(f'A media da idade do grupo é {mediai}')
print(f'As mulheres do grupo são: {lismul}')
for c in lispidades:
    if c['ida'] > mediai:
        lispmaisqmedia.append([c['nome'], c['ida']])
print(f'As pessoas que tem acima da média sao {lispmaisqmedia}')

