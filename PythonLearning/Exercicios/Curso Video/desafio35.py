reta1 = float(input('Digite a reta 1: '))
reta2 = float(input('Digite a reta 2: '))
reta3 = float(input('Digite a reta 3: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta3:
    print('As retas podem formar um triangulo')
else:
    print('As retas não formam um triangulo')
