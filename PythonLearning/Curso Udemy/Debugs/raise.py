"""
Raise!::@!:@:!@:!@:!:@!:@!$:#$!!%
Levantando os próprios erros com raise

raise -> Lança exceções

OBS: O raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra em Python.

Para simplificar, pense no raise sendo útil para que possamos criar nossas próprias esceções e mensagens de erro.

A forma geral de utilização:

raise TipoDoErro('Mensagem do erro')

# Exemplo

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Hcode', 4)

OBS: O raise assim como return, finaliza a função, ou seja, nada após o raise é executado.
"""
# Exemplo

def colore(texto, cor):
    cores = ('vermelho', 'verde', 'azul', 'branco', 'preto')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Hcode', 'cinza')
