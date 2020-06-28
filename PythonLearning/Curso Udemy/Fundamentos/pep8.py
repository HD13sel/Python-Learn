""""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a lingugagem Python.

The Zen of Python
import this

A ideia da PEP8 é que possamos escrever codigos Python de forma Pythonica.

[1] Utilize Camel Case para nomes de classes;
class Calculadora:
    pass


class CalculadoraCientifica:
    pass
[2] Utilize nomes em minusculo, separados em '_' para functions ou var;
def soma():
    pass


def soma_dois():
    pass


numero = 4


numero_impar = 5

[3] Utilize 4 espaços para identaçao (nao use tab)
if 'a' in 'banana':
    print('tem')

[4] Linhas em branco
Separar funcoes e definicoes de classe com 2 linhas em branco
Metodos dentro de uma classe devem ser separados com 1 unica linha em branco

[5] Imports
Imports devem ser feitos em linhas separadas;

#Import errado
import sys, os

#Import certo
import sys
import os
#Nao ha problems em utilizar:
from types import StringType, ListType

#Caso tenha muitos imports do mesmo pacote, recomenda fazer

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

#Imports devem ser colocados no topo de arquivo, logo depois de qualquer coment ou docstrings e antes de constantes ou
var globais;

[6] Espacos em expressoes e instrucoes

#Nao faça

funcao(_algo[_1_], {_outro: 2_}_) //Underlines !!

#Faça

funcao(algo[1], {outro: 2})

[7] Termine sempre uma instrução com uma nova linha
"""




