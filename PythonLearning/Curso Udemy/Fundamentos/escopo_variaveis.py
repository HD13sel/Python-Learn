"""
Ecopo de variáveis

Dois casos de escopo:

1- Variáveis Globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o pograma.

2- Variáveis Locais:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_de_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos
uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido aos atribuirmos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java;
int numero = 42;

"""
numero = 42  # Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Diesel'
print(numero)
print(type(numero))

nao_existo = 'Oi'
print(nao_existo)

numero = 13

if numero > 10:
    novo = numero + 10  # Exemplo de variável local
    print(novo)
