geral = list()
alunos = list()
alunosb = list()
perg = ''
pergn = 0
while perg != 'n':
    aluno = input('Aluno(a): ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    perg = input('Quer continuar? [s/n]: ')
    media = (nota1 + nota2)/2
    alunos.append([aluno, [nota1, nota2]])
    alunosb.append([aluno, media])
print('-='*40)
print(f"{'No.':<4}{'Nome':<10}{'Media':>8}")
print('-'*30)
for c, a in enumerate(alunosb):
    print(f'{c:<4}{a[0]:<10}{a[1]:>8.1f}')


print('-'*30)
while pergn != 999:
    pergn = int(input('Mostrar notas do aluno (No.): (999 Encerra) '))
    for c, al in enumerate(alunos):
        if pergn == c:
            print(f'Notas de {al[0]} são {al[1]}')
            print('-' * 40)
print('Finalizando')
print('Volte sempre...')
