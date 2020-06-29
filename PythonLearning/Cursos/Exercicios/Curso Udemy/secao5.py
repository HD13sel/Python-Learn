"""
# 1 Faça um programa que receba 2 numeros e mostre qual deles é maior.
num2 = 2, 3
print(max(num2))
# 2 Leia um numero fornecido pelo user, Se esse numero for positivo, calcule a raiz quadrada do numero
# Se o numero for negativo, mostre uma mensagem dizendo que o numero é invalido
numuser = int(float(input('Ponha um numero: ')))
if numuser > 0:
    rqdr = numuser ** 0.5
    print(f'A raiz quadrada de {numuser} é {rqdr})')
else:
    print('Numero invalido')
# 3 Leia um numero real. Se o numero for positivo imprima a raiz quadrada. Do contrario, imprima o numero ao quadrado
numuser = (float(input('Ponha um numero flutuante: ')))
if numuser > 0:
    rqdr = numuser ** 0.5
    print(f'A raiz quadrada de {numuser} é {rqdr})')
else:
    nqdr = numuser ** 2
    print(f'O numero quadrado de {numuser} é {nqdr}')
# 4 Faça um programa que leia um numero, caso positivo faça o numero ao quadrado e a raiz quadrada.
numuser = (float(input('Ponha um numero flutuante: ')))
if numuser > 0:
    rqdr = numuser ** 0.5
    nqdr = numuser ** 2
    print(f'O numero quadrado de {numuser} é {nqdr}')
    print(f'A raiz quadrada de {numuser} é {rqdr})')
# 5 Faça um programa que receba um numero inteiro e verifique se este numero é par ou impar
numuser = float(input('Ponha um numero: '))
resto = numuser % 2
if resto == 0:
    print('Número é par')
else:
    print('Número é impar')
# 6 Faça um programa que, dados dois numeros, mostre na tela o maior deles, assim como a diferença existente entre eles;
num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')
print(f'O maior numero é: {max(num1, num2)}')
print(num1, num2)
# 7 Faça um program que receba 2 numeros e mostre o maior. Se os dois numero forem iguais, imprima num iguais.
num1 = int(input('num1: '))
num2 = int(input('num2: '))
if num1 == num2:
    print('Numeros iguais')
else:
    print(max(num1, num2))
###############################################
# 8 Faca um programa que leia 2 notas de um aluno, verifique as notas são validas e exiba na tela a media dessas notas.
# Uma0, caso a nota nao seja valida, informe ao user e end.

def frange(start, stop=None, step=None):
    # if stop and step argument is None set start=0.0 and step = 1.0
    start = float(start)
    if stop == None:
        stop = start + 0.0
        start = 0.0
    if step == None:
        step = 1.0


n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
notas = n1, n2
for notas in frange(0, 10.0):
    print('Nota Valida')
    print(f'A média das notas é {n1 + n2 / 2}')
else:
    print('Nota invalida')
##################################################
# 9 Leia o salario de um trabalhado e o valor da prestacao de um emprestimo. Se a prestaca for maior que 20% do salario
# imprima: Emprestimo não concedido, caso contrário imprima: Empréstimo concedido
salario = float(input('Salario: '))
prestemp = float(input('Prestação: '))
calculo = salario * 20/100

if prestemp <= calculo:
    print('Emprestimo concedido!')
else:
    print('Emprestimo não concedido!')
# 10 Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
# homens (72.7 * h) - 58 /// mulheres (62,1 * h) - 44,7
altura = float(input('Altura: '))
sexo = input('Sexo (M)/(F): ')

if sexo == 'M':
    print(f'Peso ideal: {(72.7 * altura) - 58}')
if sexo == 'F':
    print(f'Peso ideal: {(62.1 * altura) - 44.7}')
"""




