nome = str(input('Nome: ')).capitalize()
media = float(input(f'Media de {nome}: '))
if media >= 7:
    mediasit = 'Aprovado'
elif media >= 5:
    mediasit = 'Recuperação'
else:
    mediasit = 'Reprovado'
aluno = {'Nome': nome, 'Media': media, 'Situacao': mediasit}
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
