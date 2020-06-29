dist = float(input('Qual é a distância da viagem: '))
# precopert = 0.50
# precolong = 0.45
# distmedia = 200.0
# if dist <= distmedia:
#     dista = distmedia - dist
#     mediadist = distmedia - dista
#     valor = precopert * mediadist
#     print(f'Voce vai viajar {dist}km, e vai pagar R${valor:.2f}')
# else:
#     valor = precolong * dist

valor = dist * 0.50 if dist <= 200 else dist * 0.45
print(f'Voce vai viajar {dist}km, e vai pagar R${valor:.2f}')
print('Boa viagem')
