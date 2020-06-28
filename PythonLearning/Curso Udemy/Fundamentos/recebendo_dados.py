"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
1- Aspas simples;
2- Aspas duplas;
3- Aspas simples triplas;
4- Aspas duplas triplas;

Ex:
1- 'Diesel'
2- "Diesel"
3- '''Diesel'''
"""
# 4- """Diesel"""


# Entrada de dados

# print("Qual seu nome? ")
# nome = input()  # Input -> Entrada

nome = input("Qual seu nome? ")

# Exemplo de print 'antigo' 2.x
# print('Seja bem vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem vindo(a) {0}'.format(nome))

# Exemplo de print 'atual' 3.7
print(f'Seja bem vindo(a) {nome}')

# print("Qual sua idade? ")
# idade = input()

idade = int(input('Qual sua idade? '))

# Processamento


# Saída

# print('%s tem %s anos' % (nome, idade)) (Antigo)
# print('{0} tem {1} anos'.format(nome, idade)) (Moderno)
print(f'{nome} tem {idade} anos.')  # Atual
"""
# int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""
print(f'{nome} nasceu em {2020 - idade}')
