teste = list()
teste.append('Henrique')
teste.append(25)
galera = list()
galera.append(teste[:])
teste[0] = 'Kezia'
teste[1] = 23
galera.append(teste[:])
teste[0] = 'Gabriela'
teste[1] = 24
galera.append(teste[:])
print(galera[0][1])
