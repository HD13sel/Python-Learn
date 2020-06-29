"""
Erros mais comuns em Python

É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código.

Os erros mais comuns:

SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe.
Ou seja, você escreveu algo que o Python não reconhece como parte da linguagem.

# Exemplos SyntaxError

a)
def funcao:
  print('Geek University')
b)
None = 1
c)
return

NameError -> Ocorre quando uma variável ou função não foi definida,

# Exemplos NameError

a)
print(geek)
b)
geek()
c)
a = 18
if a < 10:
  msg = 'É maior que 10'
print(msg)


TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

# Exemplos TypeError

a)
print(len(5)
b)
print('Geek' + [])

IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um
índice inválido.

# Exemplos IndexError

a)
lista = ['Geek']
print(lista[2])
b)
tupla = ('Geek')
print(tupla[0][10])

ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto
mas valor inapropriado.

# Exemplos ValueError
a)
print(int('Geek'))

KeyError -> Ocorre quando tentamos acessar um dict com uma chave que não existe.

# Exemplos KeyError
a)
dic = {'python': 'geek'}
print(dic['geek'])  >> Esta buscando a chave.

AttributeError -> Ocorre quando uma variável não tem um atributo/função.

# Exemplos AttributeError
a)
tupla = 11, 2, 31, 4
print(tupla.sort()) >> função sort() só funciona em list.

IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

# Exemplos IndentationError
a)
def nova():
print('Geek')

OBS: Exceptions e Erros são sinônimos na programação.
OBS: Importante ler e prestar atenção na saída de erro.

"""


