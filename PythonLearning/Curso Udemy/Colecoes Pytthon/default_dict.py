"""
Módulo Collections - Default Dict

# Recap Dicionários
dicionario = {'curso': 'Python'}
print(dicionario)

print(dicionario['curso'])

print(dicionario['outro'])  # ?? KeyError

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será
criada e o valor default será atribuído.

OBS: Lambdas são funções sem nome, que podem ou não receber parâmetro de entrada e retorna e valores.
"""
# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Python'

print(dicionario)

print(dicionario['outro'])  # KeyError no dict comum, mas aqui não.

print(dicionario)

