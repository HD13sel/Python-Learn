velocidadereg = float(input('Digite a velocidade que foi registrada: '))
limite = 80.0
if velocidadereg <= limite:
    print('Está no limite da velocidade')
else:
    difkm = velocidadereg - limite
    multakm = difkm * 7.00
    print(f'Você foi multado, seu valor é R${multakm}')
print('Fim')
