valores = []
for c in range(1, 6):
    valor = int(input('Digite o valor: '))
    if c == 1:
        print('Colocando ao final da lista')
        valores.append(valor)
    elif c == 2:
        if valor > valores[0]:
            print('Colocando ao final da lista')
            valores.append(valor)
        else:
            print('Colocando na posicao 0')
            valores.insert(0, valor)
    elif c == 3:
        if valor > valores[0]:
            if valor < valores[1]:
                print('Colocando na posicao 1')
                valores.insert(1, valor)
            elif valor > valores[1]:
                if valor > max(valores):
                    print('Colocando ao final da lista')
                    valores.append(valor)
                elif valor < max(valores):
                    print('Colocando na posicao 2')
                    valores.insert(2, valor)


        else:
            print('Colocando na posicao 0')
            valores.insert(0, valor)
    elif c == 4:
        if valor > valores[0]:
            if valor < valores[1]:
                print('Colocando na posicao 1')
                valores.insert(1, valor)
            elif valor > valores[1]:
                if valor < valores[2]:
                    print('Colocando na posicao 2')
                    valores.insert(2, valor)
                elif valor > valores[2]:
                    if valor < max(valores):
                        print('Colocando na posicao 3')
                        valores.insert(3, valor)
                    elif valor > max(valores):
                        print('Colocando no final da lista')
                        valores.append(valor)

        else:
            print('Colocando na posicao 0')
            valores.insert(0, valor)
    elif c == 5:
        if valor > valores[0]:
            if valor < valores[1]:
                print('Colocando na posicao 1')
                valores.insert(1, valor)
            elif valor > valores[1]:
                if valor < valores[2]:
                    print('Colocando na posicao 1')
                    valores.insert(1, valor)
                elif valor > valores[2]:
                    if valor < valores[3]:
                        print('Colocando na posicao 2')
                        valores.insert(2, valor)
                    elif valor > valores[3]:
                        if valor < max(valores):
                            print('Colocando na posicao 3')
                            valores.insert(3, valor)
                        elif valor > max(valores):
                            print('Colocando no final da lista.')
                            valores.append(valor)

        else:
            print('Colocando na posicao 0')
            valores.insert(0, valor)
print(valores)
