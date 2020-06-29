from datetime import date
from time import sleep
nome = str(input('Nome: ')).capitalize()
anodenasc = int(input('Ano de Nascimento: '))
anoatual = date.today().year
idade = anoatual - anodenasc
ctps = int(input('Carteira de Trabalho (Digite 0 se não tiver): '))
if ctps == 0:
    dados = {'Nome': nome, 'Idade': idade, 'Carteira de Trabalho': 'Não Possui'}
    for k, v in dados.items():
        print(f'{k} = {v}')
    sleep(1)
    print('Programa finalizado')
    exit()
anocontrato = int(input('Ano de Contratação: '))
salr = float(input('Salario: '))
idadecont = anocontrato - anodenasc
idadeaposent = idadecont + 35
dados = {'Nome': nome, 'Idade': idade, 'Carteira de Trabalho': ctps, 'Ano de Contrato': anocontrato, 'Salario': salr}
print('Mostrando os resultados...')
sleep(2)
for k, v in dados.items():
    print(f'{k} = {v}')
    sleep(0.8)
print(f'Vai aposentar-se com {idadeaposent}')

