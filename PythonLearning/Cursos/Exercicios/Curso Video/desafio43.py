peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é sua altura? '))

imc = peso/(altura * altura)

if imc < 18.4:
    print('Abaixo do peso.')
elif imc < 24.9:
    print('Peso ideal.')
elif imc < 29.9:
    print('Sobrepeso')
elif imc < 39.9:
    print('Obesidade')
else:
    print('Obesidade mórbida')
