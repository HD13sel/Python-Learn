"""
Len, Abs, Sum, Round

len() -> Retorna o tamanho (ou seja, o número de itens) de um iterável.

# Só pra revisar
print(len('Henrique Diesel'))
print(len([1, 2, 3]))
print(len((1, 2, 3)))
print(len({1, 2, 3}))
print(len({'a': 1, 'b': 2, 'c': 3}))
print(len(range(0, 10)))

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:

# Dunder len
print('Henrique Diesel'.__len__())


abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal.

# Exemplo Abs

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))


sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos,
incluindo o valor inicial.
OBS: O valor inicial default = 0

# Exemplos Sum

print(sum([1, 2, 3]))
print(sum([1, 2, 3], 4))
print(sum([1, 2, 3], -4))

print(sum([3.145, 5.678]))
print(sum((1, 2, 3)))
print(sum({1, 2, 3}))
print(sum({'a': 1, 'b': 2, 'c': 3}.values()))

print(sum('Henrique Diesel'))  # TypeError
print(sum('Henrique Diesel'), 'x')  # TypeError


round() -> Retorna um número arredondado para n dígito de precisão após a casa deciaml. Se a precisão não for
informada retorna o inteiro mais próximo da entrada.

"""
# Exemplo Round
print(round(10.2, 3))
print(round(10.5))
print(round(10.6))
print(round(10.554))
print(round(10.556))
print(round(1.21212121, 2))
print(round(1.219999, 2))
print(round(1.21212121))

