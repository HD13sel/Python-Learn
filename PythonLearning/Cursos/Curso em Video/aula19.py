# pessoas = {'nome': 'Henrique', 'sexo': 'M', 'idade': 25}
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# pessoas['nome'] = 'Henriq'
# pessoas['peso'] = 98.5
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
#
# print(brasil[1]['sigla'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(f'{v}/', end='')
    print()
