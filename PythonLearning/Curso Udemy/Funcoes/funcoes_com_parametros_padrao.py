"""
Funçoes com Parâmetro Padrão (Default Parameters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde o param. é opcional;
print('Henrique Diesel')
print()

# Exemplo de função onde o param. é obrigatório;

def quadrado(numero):
    return numero ** 2


print(quadrado(3))
print() # TypeError

def exponencial(numero, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))  # 2 * 2 * 2 = 8
print(exponencial(3, 2))  # 3 * 3 = 9

print(exponencial(3))  # Por padrão eleve ao quadrado
print(exponencial(3, 5))  # Eleva á potêmcia informada pelo usuário

# OBS: Se o user passar somente 1 param. este será atribuido ao param. numero, e será calculado o quadrado deste numero,
# Se o user passar 2 argumentos, o primerio será atirbuido ao param. numero e o segundo ao param. potencia.
# Então sera calculada esta potencia.

print(exponencial())

# OBS: Em funções Python, os param. com valores default (padrão) DEVEM sempre estar ao final da declaração.

# ERRO!
def teste(potencia, num=2):
    return num ** potencia

print(teste(6))

# Outros exemplos

def soma(num1=5, num2=3):
    return num1 + num2

print(soma(3, 3))
print(soma(4))
print(soma())

# Exemplo mais complexo

def mostra_info(nome='Henrique', instrutor=False):
    if nome == 'Henrique' and instrutor:
        return 'Bem-vindo instrutor Henrique!'
    elif nome == 'Henrique':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_info())
print(mostra_info(instrutor=True))
print(mostra_info(True))
print(mostra_info('Dihen'))
print(mostra_info(nome='Leseid'))

# Porque utilizar parâmetro com valor default?

- Nos permite ser mais flexíveis nas funcões;
- Evita erros com param. incorretos;
- Nos permite trabalhar com exemplos mais legiveis de código;

# Parametros default aceitam qualquer tipo de dados;
# Exemplos

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas...

# Variáveis globais
# Varáveis locais

instrutor = 'Henrique'  # Variável global


def diz_oi():
    instrutor = 'Python'  # Variável local
    return f'Oi {instrutor}'

print(diz_oi())

# OBS: se tivermos uma varável local com o mesmo nome de uma variável global, a local terá preferência.

def diz_oi():
    prof = 'Henrique'  # Variável local
    return f'Olá {prof}'

print(diz_oi())

print(prof)  # NameError


# ATENÇÃO com variáveis globais (Se puder evitar, evite!)

total = 0

def incrementa():
    total = total + 1  # UnboundLocalError (A var local está sendo utilizada para processamentos sem ter sido criada).
    return total

print(incrementa())

total = 0

# Para chamar uma var global para o escopo de uma var local, usamos (global var)

def incrementa():
    global total  # Avisando que queremos utilizar a var global,

    total = total + 1
    return total

print(incrementa())

"""

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de uma var.
# Para chamar uma var local para outro escopo, usamos (nonlocal var)
def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())

print(dentro())  # NameError

